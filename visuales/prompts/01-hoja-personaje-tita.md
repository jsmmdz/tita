# `@tita` — hoja de personaje

**Qué produce:** la hoja de tres paneles que se sube a Higgsfield como elemento
`@tita`. Es la base de todas las generaciones posteriores de la serie.

| Dato | Valor |
|---|---|
| Motor | **Nano Banana Pro** — reproduce fielmente el adjunto y sostiene la estructura de hoja `[03:32]` |
| Aspect ratio | **16:9** |
| Adjuntos | **Las fotos del traje real** (identidad) + los renders limpios de Blender (geometría) |
| Paleta | Sale de las fotos del traje. El color transfer `[08:55]` la fija para toda la serie |

---

## Quién manda: el traje, no el modelo 3D

Son dos Titas distintas, y hay que elegir una.

| | **Traje real** | **Modelo 3D** |
|---|---|---|
| Ojos | **Verde esmeralda**, grandes, esclerótica blanca | Violeta |
| Color | Verde bosque oscuro + panel crema | Gris sin texturizar |
| Cabeza | Grande respecto del cuerpo, hocico ancho y redondo | Chica, hocico corto, cuerpo esbelto |
| Cejas | Tres trazos crema sobre cada ojo | No tiene |

**Manda el traje.** Es la Tita que la comunidad de la UEB reconoce, y esta es
una pieza institucional: la identidad no se rediseña de paso. El modelo 3D
queda como **ayuda de geometría** —vistas limpias, alineadas, repetibles— pero
si las proporciones pelean, gana la foto.

> **Y hay que decirle explícitamente que NO es un disfraz.** Las fotos son de
> un traje de felpa: costuras, cierre, brillo de tela, la máscara rígida de la
> cara. Un modelo generativo copia todo eso. El prompt lo bloquea con negativos
> explícitos — se quiere un personaje animado, no una botarga.

> **Antes de subir las fotos a Higgsfield, recórtalas a Tita.** En las dos hay
> estudiantes y asistentes identificables de fondo, y en una hay un gorro de
> fiesta que no es parte del personaje. Es *"clean your plate"* `[12:01]` y de
> paso evita meter caras de terceros en un asset de producción.

---

## Antes de correrlo: qué renders hacen falta

El prompt no arregla una referencia mala. Los renders tienen que salir así:

1. **Brazos abajo, relajados a los costados. No T-pose.** Las hojas del tutorial
   dicen *"arms relaxed at sides"*. Si la referencia va en cruz, el elemento
   reproduce a Tita en cruz para siempre.
2. **Render limpio, no captura del viewport.** Sin grilla, sin cursor 3D, sin el
   punto del origen, sin las líneas de los ejes. Fondo **gris neutro plano**
   — que además es el fondo que el tutorial recomienda para todo asset `[02:31]`.
3. **Los ojos iguales en todas las vistas.** Hoy la frontal tiene iris violeta
   con pupila y la lateral un óvalo blanco con un punto. Se resuelve en Blender:
   lo que entra roto, sale roto.
4. **Tres vistas: frontal, tres cuartos y primer plano de la cara.** Son las que
   tienen foto real del traje. La trasera queda afuera a propósito: no hay
   ninguna foto de Tita de espaldas y el modelo la inventaría.
5. **Luz pareja y sin sombras duras** en las tres, para que los paneles calcen.

> ### La cola: decidida el 2026-09-08 — **Tita lleva cola**
>
> Decisión de Samuel. El traje no la tiene —no aparece en ninguna de las cuatro
> fotos, ni en la de tres cuartos, que es donde se vería— pero **el modelo 3D
> sí**, larga y gruesa, extendida hacia atrás. Va.
>
> Es la única parte del personaje donde **manda el modelo 3D y no el traje**,
> por la razón simple de que es la única fuente que hay.
>
> **Corregido el 2026-09-08 con foto del traje.** La primera versión decía
> "larga como el cuerpo, extendida hacia atrás y levantada", sacado del modelo
> 3D. **Es al revés:** la cola real es **corta, ancha y baja** — una paleta
> redondeada que cuelga hacia abajo y casi roza el piso. Verde bosque como el
> resto. La generación de Nano Banana Pro del 2026-09-08 se corrió con la
> descripción vieja y **queda invalidada por la fuente**, no por el motor.
>
> ### El logo de la UEB va en la cola — y se compone en edición
>
> La marca blanca de la cola **es el logo de la Universidad El Bosque**.
> Confirmado por Samuel, 2026-09-08.
>
> **Decisión: la hoja se genera con la cola verde lisa y el logo se compone en
> edición.** Ningún modelo lo dibuja. Las razones:
>
> - Un logo institucional reconstruido de una foto borrosa **es un problema de
>   marca**, no un defecto estético. El tutorial lo dice sin rodeos: el emblema
>   se define como elemento propio con detalle obsesivo, nunca se deja
>   reconstruir de memoria `[27:32]`.
> - **La cola es chica en cuadro y en video se mueve.** Un logo pequeño en
>   movimiento es lo primero que se rompe. En el proyecto Cartier el criterio
>   era que un emblema aguanta a partir de unos 60 px de alto en cuadro; por
>   debajo no se pide. La cola de Tita casi nunca va a llegar a eso.
>
> Consecuencia para el prompt: **la cola va verde lisa y los negativos prohíben
> explícitamente cualquier marca, letra o logo sobre ella.** Es más seguro pedir
> superficie limpia que pedir un logo y corregirlo después.
>
> Pendiente: conseguir el archivo oficial del logo de la UEB para la
> composición.

---

## El prompt

> **El color sale de las fotos del traje.** Está escrito abajo en el bloque de
> pelaje; si algo no coincide con el traje real, manda el traje.

```text
Three-panel character reference sheet on one seamless canvas, based on the 3D character in the attached renders — a stylized cartoon weasel character. Replicate her geometry 1:1 from the attached renders: exact same head shape, muzzle length, eye size and spacing, ear shape and placement, neck length, torso proportions, limb length, paw shape, tail length and thickness, and overall head-to-body ratio. The silhouette must not be reinterpreted and the geometry must not be redrawn from memory — the attached renders are the authority on form. Only the surface changes: the grey untextured clay of the renders becomes finished fur and color.

Coloring, taken from the attached costume photographs and treated as canon: deep forest green fur covering the back, flanks, outer ears, arms, legs and the top of the head, the green wrapping around the eyes as a mask that narrows toward the muzzle — a rich saturated dark green that reads almost black in shade and clearly green in sunlight. A broad warm cream panel runs from under the chin down the chest and across the belly in one continuous rounded shape. The muzzle and cheeks are the same warm cream, wide and softly rounded. The nose is large, rounded and pale salmon pink. Inner ears pale salmon pink. Hands and feet pale salmon pink with four soft digits each. Eyes very large and round with a white sclera, a bright emerald-green iris, a dark pupil and a single white catchlight. Above each eye, three short curved cream brow strokes. Long dark brown whiskers, three to a side.

Fur is rendered as soft short plush with visible large-scale grooming direction, never as fine individual strands. Eyes are large, round and glossy with a clear iris, a dark pupil and a single soft catchlight — identical size, color and spacing in every panel. Small rounded ears, short muzzle with a small dark nose, two small pointed fangs just visible at the upper lip, thin light whiskers. Warm, alert, friendly expression, mouth closed in a small natural smile. Body proportions from the attached photographs: a very large rounded head, roughly a third of her total height, sitting on a soft pear-shaped body with a wide low belly and short stubby legs. Standing upright on her hind legs, bipedal, arms relaxed down at her sides — NOT a T-pose, NOT arms outstretched, NOT arms raised. She has a short, broad, low-hanging tail — a rounded paddle shape, wider than long, narrow at the base and widening to a soft rounded end that hangs down almost to the ground. NOT long, NOT thin, NOT raised, NOT extended backward. Deep forest green like her back, completely plain and unmarked — no marking, no pattern, no emblem, no lettering.

Panel layout, left to right, all three showing the same single character at identical scale, proportions and lighting: LEFT — full-body three-quarter view, head to feet, turned about 45 degrees, showing the profile of the muzzle and the depth of the body. CENTER — full-body front view, head to feet, standing upright facing camera, arms relaxed at sides, feet flat and slightly apart. RIGHT — tight close-up portrait of her head and upper chest, looking straight into camera, face identical to the center panel.

Studio-grade 3D animation render, appealing modern feature-animation character language — NOT photoreal, NOT flat 2D cartoon, NOT a plush toy, NOT a clay or plasticine figure. Clean neutral mid-grey seamless background with no horizon line, no gradient and no vignette. Soft even shadowless illumination arriving from all directions, no key light, no rim light, no hard shadows on the character or the ground, no specular hotspots. Subtle soft contact shadow under each pose. Thin light divider lines between the three panels. Deep focus, whole figure sharp in every panel.

She is a living animated character, NOT a mascot costume and NOT a person in a suit: no fabric seams, no zippers, no stitching, no visible suit openings, no rigid mask edge around the face, no velvet or velour sheen, no foam padding shape. No clothing, no hats, no party hats, no accessories, no props, no text, no letters, no numbers, no labels, no watermarks, no logos, no grid lines, no axis lines, no 3D cursor, no viewport overlay, no user interface elements, no measurement guides. Nothing in the frame except the three panels of the character on the grey background. 16:9.
```

---

## Por qué está escrito así

| Decisión | De dónde sale |
|---|---|
| Tres paneles, cara a la derecha | La estructura de las hojas del tutorial `[03:03]` |
| **Espalda en vez de vestuario** | Las del tutorial son cara / frente / espalda **de un vestuario** — el personaje es un humano vestido. Tita no lleva ropa: lo que hay que fijar es el animal, y la espalda es donde vive la cola |
| `geometry must not be redrawn from memory` | El seguro contra el modelo que reconstruye en vez de copiar el adjunto |
| Pelaje en formas grandes, no en hebras | Es lo que peor sobrevive a 720p + escalado ×2 |
| Ojos idénticos en los tres paneles, dicho explícito | El fallo de `[08:04]`: la cara del primer plano no coincidía con la del cuerpo entero, y eso rompe los videos después |
| Negativos contra la botarga | Las fotos son de un traje de felpa. Sin bloquearlo, el modelo copia costuras, cierre y máscara rígida |
| **Con cola, corta y baja** | Foto del traje, 2026-09-08. Corrige la primera versión, que la describía larga y levantada copiando el modelo 3D |
| Negativos contra correa y costura | La foto de espaldas muestra una correa vertical y la línea del cierre: son estructura del traje, no del personaje |
| **Cola lisa, sin logo** | El logo de la UEB va en la cola pero se compone en edición. Pedirlo generado es pedir un logo institucional derretido |
| Paneles frontal / ¾ / cara | Son las tres vistas de las que hay foto real. El tutorial usa espalda, pero acá no hay referencia de la espalda y el modelo la inventaría |
| Nada de texto ni de overlay de Blender | *"Clean your plate"* `[12:01]` |
| El color va aparte | Color transfer `[08:55]`, para que forma y paleta no compitan como dos referencias |

## Después de generar

1. **Batear, no pedir una.** Una de cada cuatro sirve `[14:34]`. Se generan
   varias y se elige.
2. **Revisar que los tres paneles calcen** — misma escala, misma luz, mismos
   ojos. Si el primer plano se fue por su lado, el parche de `[08:04]` es
   recortar la cara del panel del cuerpo en un editor y usarla como fuente.
3. **Nunca encadenar ediciones.** Si hay dos cosas que arreglar, se arreglan en
   una sola pasada desde el render limpio, no sobre el resultado anterior.
4. **Subir como elemento `@tita`** y guardar el archivo con el mismo nombre,
   `tita.png`, para no traducir nombres después.
5. **Anotar la fila en `../../registro/bitacora.md`** con el motor, el prompt y
   el veredicto. Sin fila, la generación no se puede repetir.
