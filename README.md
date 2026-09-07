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
| `voces/finalistas.md` | Las seis preseleccionadas y el plan de prueba. |
| `voces/catalogo.md` | Las 114 voces preset de Higgsfield con su `voice_id`. |
| `investigacion/modelos-y-flujo.md` | Qué modelo usar, cuánto cuesta y cómo correr las pruebas. |
| `referencias/README.md` | Cómo se registran los audios de referencia (por ruta, no por archivo). |
| `registro/bitacora.md` | Qué se generó, con qué parámetros y qué resultó. |
| `guiones/` | **La serie de cortos.** Un capítulo por facultad, más el de presentación. |

## Reglas de este repo

- **Solo texto.** Los audios (`.wav`, `.mp3`, `.m4a`) se quedan afuera y se
  referencian por ruta. El `.gitignore` los bloquea.
- **Los archivos son la verdad.** Si un dato no está escrito acá, está
  pendiente. No se asume.
- **Fechas absolutas**: `2026-08-31`, nunca "ayer".
- Cada generación que valga la pena queda en `registro/bitacora.md` con su
  `voice_id` y sus parámetros. Un audio sin fila en la bitácora no se puede
  reproducir después.

## La voz

**Giselle** — `9d3128b8-dd25-5158-9bdb-2e69ac8998b9`, `voice_type: "preset"`.
Elegida por Samuel el 2026-09-07. Es la voz de Tita en todo. Ver
`voces/finalistas.md`.

## Estado

Arranque del repo: 2026-08-31.

**Hecho:** la investigación del lenguaje institucional, el texto de prueba, el
catálogo de voces, **la elección de la voz (Giselle)** y **los once guiones de
la serie**.

**Pendiente antes de generar audio:**

1. **La Ronda A** — Giselle en los cuatro motores, para decidir cuál habla
   español decente. La lanza Samuel a mano. Ver `investigacion/modelos-y-flujo.md`.
2. **Confirmar la persona** — todo está escrito con Tita en primera persona y
   lo oficial de la UEB la narra en tercera. Si va en tercera, se reescriben
   los once guiones.
3. **Las voces de los roles** — cada capítulo propone una, ninguna está
   audicionada.
