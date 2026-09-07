# Finalistas — audición de Samuel

Preseleccionadas a oído el 2026-08-31 sobre las 114 del catálogo. Las seis son
femeninas, que corresponde: Tita es una comadreja hembra.

| # | Voz | voice_id |
|---|---|---|
| 1 | Kaia | `bb9db352-f345-59f3-90b3-fa9432bcff91` |
| 2 | Zoe | `d0374db1-44b9-4f05-939e-0a9ae9dbbe6a` |
| 3 | Luna | `375a3398-e3b4-4f91-845d-42181e352899` |
| 4 | Chloe | `e9cfbbf0-4476-46be-b396-596eb774b165` |
| 5 | **Giselle** ← **elegida** | `9d3128b8-dd25-5158-9bdb-2e69ac8998b9` |
| 6 | Helena | `3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd` |

Todas `voice_type: "preset"`.

## Decisión: Giselle

**2026-09-07 — Samuel elige Giselle como la voz de Tita.** Es la voz de la
serie de cortos (`guiones/`) y de todo lo que venga después.

Se decidió **sin correr la Ronda B**, a oído sobre los previews del catálogo.
Queda escrito así, sin maquillar, porque cambia lo que todavía falta:

- **No hay comparación grabada de las seis en español.** Si algún día se
  cuestiona la elección, no existe el archivo que la respalde.
- **El filtro de lema sigue sin correr.** No se ha oído a Giselle diciendo
  línea institucional. Ver `prompts/texto-de-prueba.md`.
- **El motor todavía no está decidido.** La Ronda A sigue pendiente y sí hay
  que correrla: decide si el español suena prestado, y eso no depende de la voz.

Lo que sigue vivo de la Ronda A: **córrela con Giselle**, no con Luna. Ya no
tiene sentido probar el motor con otra voz.

## Qué falta saber de ellas

La preselección se hizo con los previews del catálogo, que **no son en
español**. Lo que ya sabemos es que el timbre gusta. Lo que no sabemos es lo
único que decide: **cómo suenan diciendo el texto de Tita en español.**

Eso ya no se va a medir para las seis: la elección está tomada. Lo que sigue
en pie es oír a **Giselle** en español, que es lo que hace la Ronda A.

## Plan de prueba

**Ronda A** — Giselle, en los cuatro motores. Decide el motor. Sigue pendiente.
**Ronda B** — ~~las seis en el motor ganador~~. **Cancelada:** la voz ya está
elegida.

Mismo `prompt` en todas: el de `prompts/texto-de-prueba.md`, sin cambiarle una
coma. Si el texto varía, la comparación no vale.

## Cómo se decide

En la Ronda A no se juzga la voz, se juzga el motor: cuál pronuncia español sin
acento prestado y cuál dice "2023" sin trabarse. Con eso caen varios de una.

Las otras cinco no se descartan del todo: quedan como **voces de los roles**
que dialogan con Tita en `guiones/`. Ahí sí siguen en juego.

Resultados a `registro/bitacora.md`. Una fila por audio.
