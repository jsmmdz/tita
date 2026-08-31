# Qué modelo usar y cómo correr las pruebas

Investigado el 2026-08-31 con `models_explore(type:'audio')`. Costos verificados
con `get_cost` sobre el texto real de `prompts/texto-de-prueba.md`.

---

## Los modelos que hay

| Modelo | Proveedor | Sirve para esto |
|---|---|---|
| `seed_audio` | ByteDance | Sí. Es el default. Único con `pitch_rate`. |
| `text2speech_v2` | Higgsfield | Sí, y da acceso a 5 motores distintos. |
| `qwen_audio_tts` | Alibaba | Quizá. Tiene `instruction`, pero ojo abajo. |
| `inworld_text_to_speech` | FAL | **No.** Solo pipeline de juegos. |
| `sonilo_music`, `mirelo_text_to_audio` | FAL | No. Música y efectos, solo juegos. |

## El hallazgo importante

**`text2speech_v2` con `variant: "elevenlabs"` es el mejor candidato para
español**, y además cuesta menos de la mitad que el default.

| Modelo | Costo por línea de 12 s |
|---|---|
| `seed_audio` | **1.0 crédito** |
| `text2speech_v2` + `elevenlabs` | **0.45 créditos** |

ElevenLabs es multilingüe de verdad, y ahí está el riesgo entero de este
proyecto: el catálogo de voces es de nombres anglosajones y **ninguna herramienta
dice en qué idioma habla cada voz**. Que Luna o Chloe suenen bien en inglés no
dice nada de cómo dicen "su calidad y su sentido".

Por eso la prueba no es "escuchar seis voces". Es **escuchar seis voces en dos
motores**: la misma `voice_id` puede sonar distinta según el motor que la
sintetice, y el español es justo donde más se separan.

### Las dos trampas del catálogo

1. **`inworld_text_to_speech` sí tiene voces marcadas en español** — Diego,
   Lupita, Miguel, Rafael, todas con etiqueta `(es)`. Es lo único del catálogo
   con idioma explícito. **Y no se puede usar:** está restringido al pipeline
   de generación de juegos. Vale saberlo por si algún día se abre.
2. **`qwen_audio_tts` tiene un parámetro `instruction`** en lenguaje natural
   para dirigir emoción, dialecto y estilo — sonaría ideal para pedir "español
   colombiano, cálida, curiosa". Pero su lista de `language` es
   `zh, en, fr, de, ja, ko, ru, pt, th, id, vi, it, ms`: **el español no está.**
   Es un hint opcional, así que igual podría funcionar, pero no lo pondría en la
   ronda principal. Una sonda suelta, si las otras dos decepcionan.

## Nota sobre créditos

`models_explore` reporta `unlim: available: false`. **No hay generaciones
ilimitadas disponibles**, así que todo sale del saldo de créditos. Las cifras
de arriba son el costo real.

## El flujo de prueba

### Ronda 1 — las 6 finalistas en los 2 motores

12 generaciones en total: 6 voces × `seed_audio` y las mismas 6 ×
`text2speech_v2/elevenlabs`.

**Costo: 8.7 créditos.** (6 × 1.0) + (6 × 0.45).

Cómo se corre, en este orden:

1. **`generate_audio_batch`** con las 6 de `seed_audio`. Una sola llamada, los
   6 jobs salen en paralelo. Cada item lleva su `index` para no perderlos.
2. **`generate_audio_batch`** otra vez con las 6 de `elevenlabs`.
3. **`jobs_wait`** con los ids devueltos, en grupos de máximo 12.
4. **`show_generation_by_ids`** — **una sola llamada con los 12**. No
   `show_generations`, no `job_display` uno por uno.

Detalle que ahorra un error: **`get_cost` no funciona dentro de un batch.**
El preflight se hace antes, con un `generate_audio` suelto y `get_cost: true`
(no envía job ni cobra). Así se sacaron las cifras de arriba.

### Ronda 2 — ajuste fino

Solo sobre la ganadora, y solo si "casi" queda. Los parámetros de
`seed_audio`, con sus rangos reales:

| Parámetro | Rango | Default |
|---|---|---|
| `speech_rate` | −50 a 100 | 0 |
| `pitch_rate` | −12 a 12 | 0 |
| `loudness_rate` | −50 a 100 | 0 |

`text2speech_v2` **no tiene ninguno de estos** — solo `variant`, `voice_type`
y `voice_id`. Ese es su costo oculto: es más barato y probablemente mejor en
español, pero si la voz sale un poco rápida o un poco aguda, no hay perilla
que mover. Con `seed_audio` sí.

**Cómo se resuelve esa tensión:** si gana una de ElevenLabs, se acepta como
viene o se arregla con puntuación en el texto. Si el ajuste resulta
indispensable, la finalista se pasa a `seed_audio` y se afina ahí.

Antes de tocar `speech_rate`, mueve las comas. La puntuación controla las
pausas y es gratis.

### Salida

Formato `wav` a `44100` Hz para la propuesta final. Para las pruebas el default
(`wav`, 24000) sobra y pesa menos.

## Recomendación

Corre la Ronda 1 completa, los dos motores. Son menos de 9 créditos y resuelve de una
la pregunta que de verdad importa — cuál motor habla español decente — en vez
de descubrirla después de haber elegido voz.
