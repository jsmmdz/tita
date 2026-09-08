# Flujo visual — Tita en cuadro

> La voz va por su lado: [`../FLUJO.md`](../FLUJO.md) y
> [`../guiones/PRUEBA-01.md`](../guiones/PRUEBA-01.md). Los guiones de
> [`../guiones/`](../guiones/) mandan sobre qué se dice; este documento define
> **cómo se ve Tita al decirlo**.

**Fuente:** el tutorial oficial de Higgsfield, *"How I Built a Car Commercial
With AI"* — transcripción, prompts y parámetros en
[`../referencias/higgsfield/`](../referencias/higgsfield/). **Cada técnica de
acá va anclada a su marca de tiempo** (`[08:55]`), para poder volver al segundo
exacto y verificarla. Es la regla que viene con el método.

**Recursos de Tita que ya existen:** el modelo 3D en Blender, las ilustraciones
a color, y los once guiones escritos.

---

## El flujo son tres pasos

> *"The whole workflow is just three steps. Assets, setup, and generations.
> Today it's a car, but the same workflow works for pretty much any
> commercial."* `[01:41]`

Y el orden no se negocia: **ningún plano se genera antes de que todos los
elementos existan.**

---

## Lo que Tita ya tiene ganado

### El modelo 3D reemplaza dos técnicas caras del tutorial

**1. La hoja de personaje no se genera: se renderiza.**

El tutorial dedica de `[03:03]` a `[08:32]` a fabricar hojas de personaje, con
rondas de casting, caras que no coinciden entre paneles y un parche manual
—recortar la cara del cuerpo entero en un editor `[08:04]`— para arreglarlo.
Todo eso existe porque el personaje solo vivía en fotos.

Tita vive en Blender. Las vistas salen de la cámara, exactas y alineadas. **El
problema de coherencia entre paneles no se arregla: no ocurre.**

**2. El render *es* el "video de estáticos".**

El truco favorito del autor `[15:00]`–`[16:03]`: para que un interior se
mantenga idéntico entre planos, genera **un video** de tomas fijas y saca un
screenshot de cada una como elemento —

> *"Every frame of a video matches every other frame by definition."* `[15:30]`

Es un rodeo para conseguir consistencia geométrica de un modelo que no la
garantiza. **Blender la garantiza por construcción.** Un turnaround renderizado
es lo mismo que ese video de estáticos, pero exacto y gratis.

### Los renders ya están en el fondo correcto

> *"Always generate the product shots on a neutral gray backdrop. It makes them
> way easier to blend into any background later."* `[02:31]`

Los renders de Blender salen sobre gris neutro. Coincide sin hacer nada.

---

## El problema del color, y cómo lo resuelve el tutorial

Los renders son **gris arcilla**; el color vive en las **ilustraciones**. Meter
las dos como referencias compitiendo es lo que devuelve un promedio.

**La respuesta está en `[08:55]`, y no es un prompt: es un ajuste.**

> *"In the image tab I'm gonna select Soul Cinema, click **color transfer** and
> upload that image. From now on every image I create pulls from that exact
> same palette. It's what keeps the whole film looking like one film."*

El color transfer **no es una referencia adjunta**. Es un estado de la
herramienta. Eso separa las dos fuentes en canales distintos, y el conflicto
desaparece:

| Canal | Fuente | Cómo entra |
|---|---|---|
| **Geometría, silueta, proporción** | El render de Blender | Elemento adjunto `@tita` |
| **Paleta y acabado** | Las ilustraciones | **Color transfer**, no adjunto |

Y viene con su propio orden de trabajo, el de `[08:32]`:

> *"My first prompts are always lazy **on purpose**. I'm not looking for the
> final location here, I just want to nail the vibe and the colors first."*

**La escalera completa:** prompt vago → se elige la imagen que da con la vibra
→ color transfer con esa imagen → recién ahí el prompt detallado.
Para Tita, la imagen de vibra sale de las ilustraciones.

---

## Elementos `@` de la serie

> *"In Higgsfield, I save it as an element with a name starting with at. Then I
> attach the same image into Claude and tell it the name. From now on Claude
> writes that name into its prompt, and when I paste the prompt back into
> Higgsfield the element attaches itself."* `[02:31]`–`[03:03]`

Dos pasos por asset, siempre. **Cada archivo se llama igual que su elemento.**

| Elemento | Qué es | De dónde sale |
|---|---|---|
| `@tita` | Hoja de tres paneles: cuerpo entero de frente, cuerpo entero de espaldas, primer plano de la cara | Renders de Blender + color transfer |
| `@tita_cola` | La cola, en su propia vista | Render lateral — **ya existe** |
| `@tita_cara` | Expresiones: neutra, sonrisa, complicidad | Se deriva de `@tita` |

**La hoja de Tita cambia respecto de la del tutorial.** Los tres paneles de
`[03:03]` son cara / frente / espalda **de un vestuario** — el personaje es un
humano vestido. Tita no lleva ropa: lo que hay que fijar es el animal. Y **la
cola es la mitad de la silueta y no se ve en el T-pose frontal**; por eso va
como elemento aparte.

**Una locación por capítulo.** Once capítulos, once sitios. Con dos reglas del
tutorial que no son opcionales:

- **A tres cuartos.** *"It's generated at a three quarter angle, which is
  really important for locations."* `[12:01]`
- **Placa limpia.** *"Anything a video model can break — melted text,
  background clutter, random cars — edit them out of the image before you
  generate a single video."* `[12:01]`. Dos pasadas de edición es lo normal
  `[12:31]`.

> ⚠️ **Y acá hay un pendiente que no es generativo.** Las locaciones son
> espacios reales de la UEB. Sin fotos de referencia el modelo inventa un
> campus, y en pieza institucional eso se nota tanto como un nombre de programa
> mal dicho. **Falta decidir: ¿campus real, o un mundo propio de Tita,
> declaradamente ilustrado?** Es dirección de arte, y define todos los prompts
> de fondo.

**Sobre el texto en cuadro:** el tutorial insiste en marcas inventadas porque no
tiene cliente. Acá pasa lo contrario — es la UEB, y el logo tendría que ser el
real. Pero el consejo de fondo se mantiene: **texto pequeño se rompe.** Si el
logo va, va grande; si no cabe grande, va en el post y no en el cuadro.

---

## ⚠️ El lip sync — y una salida que hay que probar

Los once capítulos son **Tita hablando a cámara**, y el método de voz ya
decidido es doblaje con `voice_change`. El choque:

> **`voice_change` no mira la imagen.** Solo reemplaza el audio y lo vuelve a
> pegar. No analiza labios.

Pero la transcripción cambia el panorama: **Seedance genera diálogo con la boca
sincronizada.** Toda la escena 1 del tutorial `[10:04]` es gente hablando con
sus líneas. Y `voice_change` **conserva el tiempo y la imagen**.

**Entonces existe un cuarto camino, mejor que los tres obvios:**

1. Seedance genera a Tita diciendo el guion, con labios sincronizados y su
   propia voz.
2. `voice_change` reemplaza esa voz por Giselle, **conservando el tiempo**.
3. Los labios siguen calzando, porque el tiempo no se movió.

> **Esto no está verificado.** Es una lectura de cómo se comportan las dos
> herramientas, no algo que hayamos corrido. Que `voice_change` conserve la
> duración total no garantiza que conserve el fraseo interno lo suficiente para
> que el labio aguante. **Es lo primero que hay que probar**, y es barato:
> un capítulo.

Si falla, el respaldo sigue siendo el de siempre: **Tita en off**, narradora,
haciendo cosas en cuadro en vez de hablar de frente. Los guiones ya están
escritos con una situación física por capítulo —Tita asomándose a la ventanilla
de la sala de simulación—, así que ese camino no obliga a reescribir nada.

---

## Cómo se escribe un prompt de video

Formato del skill `seedance-prompt-gen`
([`../referencias/higgsfield/seedance-prompt-gen/SKILL.md`](../referencias/higgsfield/seedance-prompt-gen/SKILL.md)),
tres bloques:

```
— REFERENCE DEFINITIONS —   @tita: ... — character appearance only. Reference.
— TECHNICAL BLOCK —         estilo · aspect ratio · duración · sonido · calidad
— PROMPT —                  SHOT 1 — ... Cut. SHOT 2 — ...   + SFX only: ...
```

Las reglas que más pesan, con su marca:

- **El conteo de planos va como regla dura.** *"Claude wrote it as a hard rule,
  exactly five shots and four cuts, no extra inserts."* `[28:02]` Sin eso el
  modelo mete insertos y el montaje se cae.
- **Primero la geografía, después la acción.** El cuerpo del prompt abre
  fijando dónde está cada cosa, y recién ahí describe qué pasa.
- **El primer plano fija el blocking.** *"Start with one that can clearly define
  who should be where."* `[21:30]`
- **Cuanto más cerrado el encuadre, menos basura.** *"If you remember one rule
  from this video, make it this one. The tighter the frame, the less slop you
  get."* `[21:00]`
- **Si el prompt carga demasiado, se parte.** *"If this is too much for one
  prompt, split it in two."* `[16:20]`
- **El aspect ratio y la duración van en el prompt. La resolución y el lote no**
  — son ajustes de la barra de Higgsfield.
- **Sin música: `SFX only`.** En esta serie manda la voz.

### Y la regla que gobierna el presupuesto

> *"One out of four worked here, and even from the winner I only took the first
> and the last shot."* `[14:34]`
>
> *"Generate multi-shot, batch a ton, and cut the best parts together."* `[21:10]`

**Una de cada cuatro.** No se genera el plano que uno quiere: se generan muchos
y se cosecha. Eso decide cómo se parten los capítulos y cuánto cuesta cada uno.

---

## Orden de ejecución

| # | Paso | Herramienta | Estado |
|---|---|---|---|
| 0 | **Carpetas.** Una por tipo de asset, una subcarpeta nueva por iteración `[02:02]` | — | ⬜ |
| 1 | **Renders de Tita** — frontal, ¾, perfil y primer plano de cara, sobre gris neutro. Falta el ¾ | Blender | ⬜ **← SIGUIENTE** |
| 2 | **Imagen de vibra** — prompt vago, elegir la que da con el color de Tita `[08:32]` | Nano Banana Pro | ⬜ |
| 3 | **Color transfer** con esa imagen `[08:55]` | Ajuste | ⬜ |
| 4 | **`@tita`** — la hoja de tres paneles, ya a color | Nano Banana Pro | ⬜ |
| 5 | **Prueba de lip sync** — un capítulo por Seedance + `voice_change` | Seedance | ⬜ |
| 6 | **Decidir el mundo** — campus real o ilustrado | — | ⬜ |
| 7 | **Locación de `01-medicina`** — a ¾, placa limpia, dos pasadas | Nano Banana Pro | ⬜ |
| 8 | **Capítulo 01 en video** | Seedance | ⬜ |
| 9 | Los otros diez | Seedance | ⬜ |

**El capítulo 01 es la prueba visual**, igual que ya es la prueba de voz: tiene
los dos riesgos —la enumeración de programas y el remate— y si aguanta ahí,
aguanta la serie.

**El paso 5 va antes que el 7 a propósito.** Si el lip sync no funciona, toda la
serie cambia de lenguaje visual —Tita en off en vez de a cámara— y las
locaciones se piden distinto. Probarlo antes de gastar en fondos es lo que
evita rehacerlos.

---

## Reglas heredadas que no se discuten

- **Nunca encadenar ediciones.** Cada corrección sale de la fuente limpia, nunca
  del resultado de la corrección anterior. Escalar no recupera lo que se
  perdió, y lo que el modelo reinvente se vuelve canon en once capítulos.
- **No sacar todo de un solo modelo.** *"Don't try to get everything out of one
  model."* `[05:30]` Nano Banana Pro para hojas y para reproducir un adjunto;
  Seedream para tocar un detalle sin mover el resto; Seedance para el video.
- **El casting sigue siendo casting.** *"If the face doesn't feel like a lead,
  don't settle, keep iterating."* `[11:30]` Vale para las expresiones de Tita.
- **`use_unlim` se deja sin poner**, salvo que Samuel pida las ilimitadas: así
  el servidor pregunta antes de gastar.

---

## Qué falta decidir

1. **El mundo de Tita** — campus real de la UEB o ilustrado. Bloquea toda
   locación.
2. **Aspect ratio.** Los guiones apuntan a redes, lo que sugiere 9:16, pero no
   está escrito en ningún lado del repo. Va en el prompt.
3. **Presupuesto** — ¿720p + escalado ×2 y lote de 2, o hay margen para más?
   Si aplica el criterio conservador: **el pelaje y los bigotes se piden en
   formas grandes**, no en textura fina, que es lo que peor sobrevive al
   escalado.
4. **Si el modelo se puede texturizar en Blender.** Si se puede, el color
   transfer deja de ser necesario para la hoja y el camino se acorta.

Nada de esto es generativo. Son decisiones que van **antes** del primer prompt.
