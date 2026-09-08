# Técnica de Higgsfield — extraída del canal oficial

Lo que hay acá **no es de Tita**: es el método de producción sacado del
tutorial oficial de Higgsfield, traído para no reinventarlo.

**Fuente:** Higgsfield — *"How I Built a Car Commercial With AI"*
<https://www.youtube.com/watch?v=GNxmt_4IifA> · 35:47 · transcrito el 2026-08-27.

Se extrajo originalmente en el proyecto de la hackathon de Seguros Bolívar
(`jsmmdz/parchate-seguros-bolivar`, repo privado). **Acá se copió solo el
material derivado del video** — nada del contenido creativo de ese cliente.

## Qué hay

| Archivo | Qué es |
|---|---|
| `transcripcion-car-commercial.md` | La transcripción del tutorial, con marca de tiempo cada 30 s. Es la fuente que se cita |
| `prompts-oficiales-car-commercial.md` | Los prompts que el autor usa en el video, tal cual |
| `ui-parametros/INDICE.md` | Doce momentos clave: la captura de la interfaz cruzada con lo que se dice en ese segundo. **Es donde están los parámetros reales de la barra de Higgsfield** |
| `extraer-tecnica-de-video.md` | El método para sacar técnica de un video: Whisper local + ffmpeg + cruce de frames con transcripción. Reutilizable con cualquier tutorial |
| `seedance-prompt-gen/SKILL.md` | Skill que arma prompts de Seedance 2.0 en formato *All-in-One Reference*, con la estructura de bloques del tutorial |

## La regla que viene con esto

Del método original, y se mantiene:

> **Ningún parámetro entra a un prompt del proyecto sin quedar anclado a una
> marca de tiempo de la referencia.** Al citar la técnica se escribe la marca
> (`[12:05]`) para poder volver al segundo exacto y verificarla.

## Qué NO se trajo, y por qué

- **`flujo/01-ajustes-desde-la-referencia.md` y `flujo/02-etapa0-assets-y-carpetas.md`.**
  Mezclan el método con el contenido creativo de Seguros Bolívar — la pieza
  "EL TUBO", el emblema de la marca, las hojas de personaje del plomero y de
  Santiago. Ese repo es privado y `tita` es público, así que el material de
  cliente se queda allá. La parte de método de esos documentos está resumida
  en [`../../visuales/FLUJO-VISUAL.md`](../../visuales/FLUJO-VISUAL.md).
- **`referencias/frames/higgsfield-car-commercial/`** — 109 frames, 12 MB. El
  índice de `ui-parametros/` es la selección curada de esos, con los doce
  momentos que importan. Si hace falta un frame puntual, está en el repo
  privado.

## Nota sobre el "solo texto" del repo

El `README.md` de `tita` dice que el repo es solo texto. **Estos doce `.jpg`
son la excepción** (1,3 MB): son capturas de la interfaz de Higgsfield, y sin
ellas el índice de parámetros no dice nada — el texto describe lo que se ve en
la imagen. La regla sigue valiendo para el audio y el video de la serie, que es
lo que la motivó.
