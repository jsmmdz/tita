# Finalistas — audición de Samuel

Preseleccionadas a oído el 2026-08-31 sobre las 114 del catálogo. Las seis son
femeninas, que corresponde: Tita es una comadreja hembra.

| # | Voz | voice_id |
|---|---|---|
| 1 | Kaia | `bb9db352-f345-59f3-90b3-fa9432bcff91` |
| 2 | Zoe | `d0374db1-44b9-4f05-939e-0a9ae9dbbe6a` |
| 3 | Luna | `375a3398-e3b4-4f91-845d-42181e352899` |
| 4 | Chloe | `e9cfbbf0-4476-46be-b396-596eb774b165` |
| 5 | Giselle | `9d3128b8-dd25-5158-9bdb-2e69ac8998b9` |
| 6 | Helena | `3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd` |

Todas `voice_type: "preset"`.

## Qué falta saber de ellas

La preselección se hizo con los previews del catálogo, que **no son en
español**. Lo que ya sabemos es que el timbre gusta. Lo que no sabemos es lo
único que decide: **cómo suenan diciendo el texto de Tita en español.**

Por eso la Ronda 1 las corre a las seis en dos motores. El detalle está en
`investigacion/modelos-y-flujo.md`.

## Plan de prueba

Dos rondas, lanzadas a mano en la interfaz. El detalle en
`investigacion/modelos-y-flujo.md`.

**Ronda A** — una sola de estas seis, en los cuatro motores. Decide el motor.
**Ronda B** — las seis, en el motor ganador. Decide la voz.

Mismo `prompt` en todas: el de `prompts/texto-de-prueba.md`, sin cambiarle una
coma. Si el texto varía, la comparación no vale.

## Cómo se decide

En la Ronda A no se juzga la voz, se juzga el motor: cuál pronuncia español sin
acento prestado y cuál dice "2023" sin trabarse. Con eso caen varios de una.

En la Ronda B sí se comparan las seis entre sí, con los criterios de
`prompts/texto-de-prueba.md`.

Resultados a `registro/bitacora.md`. Una fila por audio.
