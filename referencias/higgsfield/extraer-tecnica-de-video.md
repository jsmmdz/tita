# Flujo de referencia: transcripción local + frames

> Añadido el 2026-08-28. Cambia la forma en que el proyecto consume tutoriales
> y material de referencia en video.

## Por qué

Hasta ahora la referencia se leía **solo por frames**: se miraba el video, se
sacaban capturas y se copiaban los parámetros que se veían en pantalla. Eso
pierde la mitad de la información — el porqué de cada ajuste, el orden real de
los pasos, las advertencias que el autor dice de paso y nunca escribe.

El flujo nuevo extrae **las dos capas**:

| Capa | Qué aporta | Herramienta |
|---|---|---|
| **Audio → texto** | El razonamiento, el orden de los pasos, los nombres exactos de menús y modelos | Whisper large-v3 local |
| **Video → frames** | Lo que se ve: la UI, los valores de los sliders, el resultado del render | ffmpeg |
| **Cruce de ambas** | Cada frame con lo que se dice en ese segundo | `tools/frames_con_texto.py` |

Todo corre **en local**. Ni el video ni el audio salen de la máquina.

## Requisitos

```bash
# audio y frames
sudo apt-get install -y ffmpeg          # macOS: brew install ffmpeg

# transcripción (uno de los dos; faster-whisper es el recomendado)
pip install faster-whisper
# alternativa, implementación de referencia de OpenAI:
pip install openai-whisper

# descarga de video, si la fuente es YouTube
pip install yt-dlp
```

La primera ejecución descarga el modelo `large-v3` (~3 GB) y lo cachea. Con GPU
tarda minutos; en CPU, del orden de 1–2× la duración del video.

## Los tres pasos

### 1. Traer el video

```bash
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best" \
       -o "referencias/video/%(title)s.%(ext)s" "<URL del video>"
```

Si ya se tiene el archivo, basta con dejarlo en `referencias/video/`.

### 2. Transcribir con máxima fidelidad

```bash
python3 tools/transcribir.py referencias/video/tutorial.mp4 \
    --slug higgsfield-tutorial --idioma en
```

Qué hace por dentro, y por qué así:

- **Extrae el audio a WAV 16 kHz mono PCM.** Es el formato nativo de Whisper:
  subir la tasa de muestreo no añade fidelidad porque el modelo remuestrea a
  16 kHz de todas formas. Guarda además un **FLAC sin pérdida** del audio
  original por si hay que volver a la fuente.
- **Modelo `large-v3`**, el más preciso de la familia.
- **`beam_size` / `best_of` 8 con `patience` 2.0** — busca mucho más ancho que
  el greedy por defecto. Es más lento y más exacto.
- **Escalera de temperaturas 0.0 → 1.0.** Si un bloque sale con logprob bajo o
  con la relación de compresión disparada (la firma de un bucle), reintenta con
  más temperatura en vez de dar por bueno el resultado malo.
- **`condition_on_previous_text=False`.** Evita que un error se arrastre al
  resto de la transcripción, el fallo más común de `large-v3` en videos largos.
- **Timestamps por palabra**, no solo por frase — es lo que permite cruzar con
  los frames.
- **Filtro VAD** para no alucinar texto sobre los silencios. Si recorta habla
  real (voz muy baja, música encima), se desactiva con `--sin-vad`.
- **`--prompt-inicial` con un glosario del proyecto** (Higgsfield, Soul ID,
  Nano Banana Pro, keyframe…). Sesga el vocabulario y sube mucho el acierto en
  la jerga y los nombres propios, que es justo donde Whisper falla.

Salidas en `referencias/transcripciones/<slug>/`:

| Archivo | Uso |
|---|---|
| `<slug>.md` | **Lectura humana.** Párrafos con marca de tiempo cada 30 s |
| `<slug>.json` | Segmentos y palabras con timestamps y confianza. Es la entrada del paso 3 |
| `<slug>.srt` / `.vtt` | Subtítulos, para revisar sobre el video |
| `<slug>.txt` | Texto corrido |
| `<slug>.wav` / `.flac` | Audio extraído (no se versiona) |

### 3. Cruzar frames con lo que se dice

```bash
# barrido: un frame cada 30 s
python3 tools/frames_con_texto.py referencias/video/tutorial.mp4 \
    --transcripcion referencias/transcripciones/higgsfield-tutorial/higgsfield-tutorial.json \
    --cada 30 --slug higgsfield-tutorial

# o solo los momentos que importan, ya localizados leyendo el .md
python3 tools/frames_con_texto.py referencias/video/tutorial.mp4 \
    --transcripcion .../higgsfield-tutorial.json \
    --marcas 3:41 12:05 19:11 --slug higgsfield-tutorial
```

Genera `referencias/frames/<slug>/INDICE.md`: cada bloque es un momento del
video con su captura y la frase exacta que se dice ahí. Ese índice es el
documento que se lee para extraer la técnica.

## Cómo entra esto en el flujo de la campaña

```
Tutorial / referencia en video
        │
        ├─ audio → transcripción (qué se explica, en qué orden)
        └─ video → frames        (qué se ve: parámetros reales de la UI)
                    │
                    └─ INDICE.md cruzado
                              │
                              ▼
              Técnica extraída y contrastada
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
  historias/03           historias/02          flujo/ (este doc)
  Soul ID Santiago       prompts de frames     ajustes al método
```

La regla: **ningún parámetro entra a los prompts del proyecto sin quedar
anclado a una marca de tiempo de la referencia.** Al citar la técnica en
`historias/02` o `historias/03`, se escribe la marca (`[12:05]`) para poder
volver al segundo exacto y verificarla.

## Qué se versiona y qué no

- **Sí:** transcripciones (`.md`, `.json`, `.srt`, `.vtt`, `.txt`), frames
  (`.jpg`) e índices. Son ligeros y son la fuente que se cita.
- **No:** los videos y el audio extraído (`.mp4`, `.wav`, `.flac`). Están en
  `.gitignore` — pesan y siempre se pueden regenerar desde la fuente.
