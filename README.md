# Tita — voz

Respaldo del flujo para generar la nueva voz de **Tita**, la mascota de la
Universidad El Bosque, usando Higgsfield.

Este repo no guarda audio. Guarda **el flujo, los prompts, los parámetros y la
bitácora de lo que se probó**, para que cualquier generación se pueda repetir
igual sin depender de la memoria de nadie.

## Qué hay acá

| Ruta | Qué es |
|---|---|
| `FLUJO.md` | El procedimiento paso a paso. Es el documento que manda. |
| `prompts/guion-base.md` | Las líneas que se usan para probar y comparar voces. |
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

Arranque del repo: 2026-08-31. Todavía no se ha creado ninguna voz.
