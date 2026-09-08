# Bitácora de generaciones

Una fila por tanda. Si no está acá, no se puede repetir.

## Voces en uso

No se creó ninguna voz: todas son presets del catálogo.

| Personaje | Voz | voice_id | Estado |
|---|---|---|---|
| **Tita** | Giselle | `9d3128b8-dd25-5158-9bdb-2e69ac8998b9` | **Elegida** 2026-09-07 |

**Habla Tita y nadie más.** No hay segundas voces en la serie: los once
capítulos son monólogo, así que es un video por capítulo y una sola conversión.

## Generaciones

| Fecha | Capítulo | voice_id | Toma | Archivo | Veredicto |
|---|---|---|---|---|---|
| _(vacío)_ | | | | | |

- **Capítulo**: el archivo de `guiones/`, por ejemplo `01-medicina`.
- **Toma**: cuál grabación original se convirtió, si hubo varias.
- **Archivo**: ruta local donde quedó el audio. No se sube al repo.
- **Veredicto**: qué falló y en cuál réplica. "Bien" no sirve de nota;
  "se come el 'cuarenta y uno', la pregunta no sube" sí.

### Líneas que hay que escuchar con lupa

Salen de las notas de locución. Son los puntos donde la conversión se puede
caer.

| Guion | Qué revisar |
|---|---|
| `02-creacion-comunicacion` | **Los siete programas seguidos.** La línea más difícil de la serie. |
| `01-medicina` | **"Medicina, Instrumentación Quirúrgica y Optometría"** y el punto y coma del remate. |
| `09-economicas` | **Las dos "y" seguidas** de la línea de programas. |
| `06-ciencias` | **"Estadística"** — esdrújula que algunos motores aplanan. |
| `07-ingenieria` | **"…todavía"** — la pausa antes y el tono. Todo el capítulo cuelga de ahí. |
| `00-presentacion` | La enumeración de cuatro comas. |

## Decisiones tomadas

Acá van los valores que ya se aprobaron y no se vuelven a discutir.

| Fecha | Decisión |
|---|---|
| 2026-08-31 | **No se clona ninguna voz.** Se usa un preset del catálogo. |
| 2026-08-31 | **Qwen queda fuera**: su interfaz no deja seleccionar la voz. |
| 2026-09-07 | **La voz de Tita es Giselle** (`9d3128b8-dd25-5158-9bdb-2e69ac8998b9`). Sin Ronda B, a oído. No se vuelve a discutir. |
| 2026-09-07 | **La serie es de once capítulos**: diez facultades más presentación. Techo de treinta segundos cada uno. |
| 2026-09-07 | **Los once capítulos son monólogo de Tita.** No hay segundas voces ni personajes. Un video por capítulo, una conversión. |
| 2026-09-07 | **Tita habla en primera persona.** Cierra el pendiente que podía reescribir los once guiones. |
| 2026-09-07 | **Los diez capítulos de facultad invitan a conocer la facultad y sus programas**, en cuatro tiempos: el nombre, qué se estudia, el giro, la invitación. |
| 2026-09-07 | **Todos abren presentando la facultad**: "Esta es la Facultad de…", nombre completo y silencio después. |
| 2026-09-07 | **La facultad se nombra una sola vez, al inicio.** El cierre no repite el nombre ni lleva "ven a conocerla": termina en una frase citable. El llamado a la acción va en el copy del post, no en la voz. |
| 2026-09-07 | **Orden de la serie:** Medicina primero, Creación y Comunicación segundo, y de ahí para abajo los demás. |
| 2026-09-07 | **La serie se hace doblando voz real**, no generando desde texto. Motivo: expresividad — el TTS todavía suena robótico y los guiones viven de las pausas. Solo la pista de Tita se convierte. |
| 2026-09-07 | **Las Rondas A y B quedan canceladas.** `voice_change` no tiene parámetro de modelo, así que no hay motor que elegir. |
| 2026-09-07 | **Los videos de entrada pueden ir en negro total.** `voice_change` no mira la imagen. El micrófono sí importa. |

### Todavía sin decidir

- **Si `voice_change` conserva la dicción.** Lo resuelve la Prueba 1 sobre
  `01-medicina`. Ver `guiones/PRUEBA-01.md`.
- **Los nombres de los programas.** Ninguno verificado contra la página oficial.
  Es el pendiente más urgente.
- **Si Giselle aguanta el lema.** Filtro sin correr.

---

## 2026-09-08 — Ronda visual 1: hoja de personaje `@tita`

**Qué se probó:** el mismo prompt de hoja de personaje en dos motores, para
decidir cuál sostiene la estructura de tres paneles. Es el método de `[04:30]`
del tutorial: mismo prompt, dos modelos, se compara.

**Prompt:** `visuales/prompts/01-hoja-personaje-tita.md`. Tres paneles —
frontal, tres cuartos y primer plano de cara. Sin cola.

**Adjuntos:** cuatro imágenes subidas por Samuel.

| media_id | Archivo |
|---|---|
| `7f1c447b-989c-41af-9955-e641d77a2e98` | Captura 2026-09-07 225224 |
| `c8a198d0-cda4-44b2-acd4-2832ece22abe` | Captura 2026-09-07 225231 |
| `809937c2-7094-4b51-b2c5-dd135116e9d2` | Captura 2026-09-07 233602 |
| `2a82cd2e-97ae-45b8-a78e-98d3da74ed8d` | Captura 2026-09-07 234219 |

> **No está confirmado cuáles son fotos del traje y cuáles renders 3D.** El
> prompt se blindó por eso: dice que las fotos del traje mandan en identidad y
> color, y que cualquier render gris sirve solo para silueta — nunca para los
> ojos, que son verdes y no violeta.

**Las dos generaciones:**

| Motor | `model` | Resolución | Aspect | Job |
|---|---|---|---|---|
| Nano Banana Pro | `nano_banana_pro` | `2k` | 16:9 | `116ad652-9dd9-40b3-a60c-a7c12c255c98` |
| Seedream 5.0 Pro | `seedream_v5_pro` | `1.5k` | 16:9 | `f7d0ffac-f460-45cd-9332-341057495e13` |

`count: 1` cada uno, `use_unlim` sin poner. Saldo antes: **1838,73 créditos**,
plan Ultra.

**Resoluciones reales del catálogo** — consultadas, no supuestas:

- `nano_banana_pro`: `1k` · `2k` · `4k`
- `seedream_v5_pro`: `1k` · `1.5k` · `2k`
- `seedance_2_0` (video): `480p` · `720p` · `1080p` · `4k`. **No tiene 1.5K.**

**Qué mirar en el resultado:**

1. ¿Los tres paneles calzan en escala, luz y ojos? Es lo que decide si sirve
   como hoja. Nano Banana Pro debería ganar acá `[03:32]`.
2. ¿Los ojos salieron verdes o se colaron los violeta del modelo 3D?
3. ¿Se lee como personaje animado o como botarga — costuras, cierre, borde de
   máscara?
4. ¿Respetó "sin cola"?
5. ¿Se coló el gorro de fiesta, el letrero o alguna persona de fondo? Las fotos
   fueron **sin limpiar la placa**, así que esto es lectura de primera ronda y
   no el asset final.

**Veredicto: invalidada por la fuente, no por el motor.** La cola se describió
larga, levantada y extendida hacia atrás, copiando el modelo 3D. La foto del
traje que Samuel pasó después muestra lo contrario. Las dos generaciones de
esta ronda pedían un personaje equivocado, así que no dicen nada sobre qué
motor es mejor.

---

## 2026-09-08 — Ronda visual 2: hoja de personaje, cola corregida

**Qué cambió respecto de la ronda 1:**

1. **La cola.** De "larga como el cuerpo, extendida y levantada" a **corta,
   ancha y baja** — paleta redondeada que cuelga y casi roza el piso. Fuente:
   foto del traje, 2026-09-08.
2. **La cola va lisa.** La marca blanca **es el logo de la Universidad El
   Bosque**. Decisión de Samuel: no se genera, se compone en edición. Los
   negativos prohíben explícitamente cualquier marca, letra o emblema encima.
3. **Negativos nuevos** contra la correa vertical de la espalda y la línea del
   cierre, visibles en la foto trasera: son estructura del traje.
4. **Dos variantes por motor** en vez de una, según *"batch a ton and cut the
   best parts together"* `[21:10]`.

| Motor | `model` | Resolución | Jobs |
|---|---|---|---|
| Nano Banana Pro | `nano_banana_pro` | `2k` | `10e45bf9-883c-4151-8b73-96c657d67a28` · `9aee2abf-0ecf-4b29-b5e6-ede75207c2f1` |
| Seedream 5.0 Pro | `seedream_v5_pro` | `1.5k` | `757d01c6-6231-4cb7-a9fe-83f3d9021a6f` · `a6dc5ae0-76fc-4706-8c18-432fd5429f86` |

Mismos cuatro `media_id` de la ronda 1. 16:9, `count: 2`, `use_unlim` sin poner.

> ⚠️ **Las fotos de la cola NO están subidas como `media_id`.** La cola va
> descrita solo con texto y el modelo no la ve. Es la parte más frágil de esta
> ronda: si la cola no calza, la causa probable es esa y no el motor.

**Qué mirar:**

1. ¿Los tres paneles calzan en escala, luz y ojos?
2. ¿La cola salió corta y baja, o volvió a salir larga?
3. ¿Quedó lisa, o el modelo le inventó una marca encima?
4. ¿Ojos verdes o se colaron los violeta del modelo 3D?
5. ¿Personaje o botarga — costuras, cierre, borde de máscara?

**Veredicto:** _(pendiente)_

---

## 2026-09-08 — Ronda 3: outfits sobre `@TITA`

**Hito:** `@tita` existe como Element — `TITA`,
`7189d8d4-c405-4a57-a505-7852b5099154`, construido sobre el job `9aee2abf`
(variante B de Nano, ronda 2, cola corta). Ese es el canon del personaje.

**Método:** cada outfit es una **edición de la hoja de personaje**, no un
personaje nuevo. Mismos paneles, mismo fondo, misma luz; cambia solo el
vestuario. Es como el tutorial hace la versión de incógnito `[06:05]`.

**Motor:** `nano_banana_pro`, 2K, 16:9, `count: 2`. Elegido sobre Seedream por
dos razones: al editar, Nano conserva mejor la cara `[06:33]`, y
**`seedream_v5_pro` no acepta Elements**.

| Outfit | Jobs |
|---|---|
| Navidad — traje completo de Santa | `e9ca791c-26c7-42c2-8c51-9a9ca77c991c` · `e3fcf0af-fae3-4be6-b326-fed775b60cd0` |
| Halloween — bruja | `0ea9941b-d8db-454f-975c-b081de0f4a1c` · `bb39580e-6a39-4151-913d-2013c9b8bd9a` |
| Halloween — calabaza | `97f44166-8fda-47ee-b537-a9354004856b` · `4647f4db-5c92-4cc9-97c6-cde5cce2c006` |

Prompts completos en `visuales/prompts/02-outfits.md`.

**Dos cosas que se aprendieron y valen para todo lo que sigue:**

1. **`nano_banana_pro` sí ruteó bien esta vez.** En las rondas 1 y 2 pedí
   `nano_banana_pro` y el backend registró `nano_banana_2` en las seis. Acá,
   con el Element embebido en el prompt, quedó `nano_banana_pro`. La
   comparación Nano-vs-Seedream de las rondas 1 y 2 **no fue contra Nano Pro**.
2. **Prompts cortos.** La ronda 2 salió peor que la 1 por exceso de negativos.
   Estos van en descripción positiva con un solo renglón de negativos.

### Comparación con Seedream 4.5

Samuel señaló que **Seedream es mejor para ropa**, y tiene razón: está en la
transcripción — *"Seedream Pro 5.0, it's one of the best models for outfits,
especially when feeding in your own inputs"* `[03:32]`.

Pero **`seedream_v5_pro` no acepta Elements**, así que no puede ver a `@TITA`.
El Seedream más alto que sí los acepta es **4.5**. Se corrieron los tres
outfits ahí con los prompts idénticos, para que el único cambio sea el motor.

| Outfit | Nano Banana Pro `2k` | Seedream 4.5 `basic` |
|---|---|---|
| Santa | `e9ca791c` · `e3fcf0af` | `4c7c4898-1fb2-413d-8f11-ab9d300c0752` · `c8073c89-3b3b-4515-85a8-117c0551804b` |
| Bruja | `0ea9941b` · `bb39580e` | `242887bb-e83a-49f0-bf3e-6e5046c742d6` · `16c5fa77-9d65-49b2-ab05-2c16361166a9` |
| Calabaza | `97f44166` · `4647f4db` | `17ede455-5d09-4714-9ecd-02a89515e9a0` · `38abfb48-c0d0-46b9-901e-653c3d4c6581` |

**Esta sí es la comparación limpia que las rondas 1 y 2 no fueron:** mismo
prompt, mismo Element, mismos tres paneles, y los dos modelos confirmados en la
respuesta del servidor. Doce imágenes en total.

**Qué mirar, en este orden:**

1. **¿La cara sigue siendo Tita?** Es lo único que no se puede perder. Según el
   tutorial, acá gana Nano `[06:33]`.
2. **¿La tela se ve bien?** Terciopelo, felpa blanca, forro naranja. Acá
   debería ganar Seedream `[06:33]`.
3. **¿Los tres paneles calzan entre sí?**
4. **¿El negro de Halloween se fundió con el verde, o el ribete naranja lo
   salvó?**

Lo esperable, si el tutorial acierta, es un empate dividido: **Nano para la
cara, Seedream para el traje.** Y si sale así, el camino es el mismo que usa el
autor con el face swap `[05:30]`: *"don't try to get everything out of one
model"* — tomar el traje de Seedream y la cara de Nano.

**Veredicto:** _(pendiente)_
