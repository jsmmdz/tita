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

## Plan de la Ronda 1

12 generaciones, 8.7 créditos:

- Las 6 con `model: "seed_audio"` — 1.0 crédito cada una.
- Las 6 con `model: "text2speech_v2"`, `variant: "elevenlabs"` — 0.45 cada una.

Mismo `prompt` en las doce: el de `prompts/texto-de-prueba.md`, sin cambiarle
una coma. Si el texto varía, la comparación no vale.

## Cómo se decide

Primero se compara **motor contra motor** con la misma voz: ¿cuál de los dos
dice "su calidad y su sentido" como lo diría alguien de Bogotá? Eso descarta un
motor entero y deja seis audios en vez de doce.

Después se comparan las seis entre sí, con los criterios de
`prompts/texto-de-prueba.md`. El lema es el que descarta.

Resultados a `registro/bitacora.md`. Una fila por audio.
