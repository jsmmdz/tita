# Tita — voz

Respaldo del flujo para proponer la nueva voz de **Tita**, la comadreja
mascota de la Universidad El Bosque, usando Higgsfield.

**No se clona ninguna voz.** Se elige una del catálogo de presets y se
propone.

Este repo no guarda audio. Guarda **el flujo, los prompts, los parámetros y la
bitácora de lo que se probó**, para que cualquier generación se pueda repetir
igual sin depender de la memoria de nadie.

## Qué hay acá

| Ruta | Qué es |
|---|---|
| `FLUJO.md` | El procedimiento paso a paso. Es el documento que manda. |
| `investigacion/lenguaje-institucional-ueb.md` | Quién es Tita y cómo habla la UEB. La base de todo lo demás. |
| `prompts/texto-de-prueba.md` | El texto con el que se audicionan las voces. |
| `voces/catalogo.md` | Las 114 voces preset de Higgsfield con su `voice_id`. |
| `referencias/README.md` | Cómo se registran los audios de referencia (por ruta, no por archivo). |
| `registro/bitacora.md` | Qué se generó, con qué parámetros y qué resultó. |

## Reglas de este repo

- **Solo texto.** Los audios (`.wav`, `.mp3`, `.m4a`) se quedan afuera y se
  referencian por ruta. El `.gitignore` los bloquea.
- **Los archivos son la verdad.** Si un dato no está escrito acá, está
  pendiente. No se asume.
- **Fechas absolutas**: `2026-08-31`, nunca "ayer".
- Cada generación que valga la pena queda en `registro/bitacora.md` con su
  `voice_id` y sus parámetros. Un audio sin fila en la bitácora no se puede
  reproducir después.

## Estado

Arranque del repo: 2026-08-31.

Hecho: la investigación del lenguaje institucional, el texto de prueba y el
catálogo de voces. Pendiente: la audición, que la hace Samuel a oído en
Higgsfield.
