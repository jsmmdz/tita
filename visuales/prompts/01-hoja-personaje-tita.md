# `@tita` — hoja de personaje

**Qué produce:** la hoja de tres paneles que se sube a Higgsfield como elemento
`@tita`. Es la base de todas las generaciones posteriores de la serie.

| Dato | Valor |
|---|---|
| Motor | **Nano Banana Pro** — reproduce fielmente el adjunto y sostiene la estructura de hoja `[03:32]` |
| Aspect ratio | **16:9** |
| Adjuntos | Los renders limpios de Blender |
| Paleta | Por **color transfer** con una ilustración, no por adjunto `[08:55]` |

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
4. **Tres vistas:** frontal, trasera y primer plano de la cara. La trasera es la
   que muestra la cola, que es media silueta y no se ve de frente.
5. **Luz pareja y sin sombras duras** en las tres, para que los paneles calcen.

> **La cola.** En el render lateral sale extendida hacia atrás, horizontal. En
> la vista trasera hay que decidir si va así o caída. Sea cual sea, **es la
> pose que Tita va a tener en toda la serie**: el elemento la fija.

---

## El prompt

> **Falta un dato y va marcado `[COLOR]`.** No hay ninguna descripción del
> color de Tita en el repo y las ilustraciones no están acá. Reemplazá ese
> bloque por el pelaje real —dorso, vientre, hocico, orejas, punta de la cola—
> antes de correrlo. Si no, Nano Banana Pro se lo inventa y esa invención queda
> de canon en los once capítulos.

```text
Three-panel character reference sheet on one seamless canvas, based on the 3D character in the attached renders — a stylized cartoon weasel character. Replicate her geometry 1:1 from the attached renders: exact same head shape, muzzle length, eye size and spacing, ear shape and placement, neck length, torso proportions, limb length, paw shape, tail length and thickness, and overall head-to-body ratio. The silhouette must not be reinterpreted and the geometry must not be redrawn from memory — the attached renders are the authority on form. Only the surface changes: the grey untextured clay of the renders becomes finished fur and color.

[COLOR] — describe here: fur color of the back and flanks, belly and chest, muzzle and cheeks, inner ears, paws, and tail tip; eye iris color; whether there are markings.

Fur is rendered as soft short plush with visible large-scale grooming direction, never as fine individual strands. Eyes are large, round and glossy with a clear iris, a dark pupil and a single soft catchlight — identical size, color and spacing in every panel. Small rounded ears, short muzzle with a small dark nose, two small pointed fangs just visible at the upper lip, thin light whiskers. Warm, alert, friendly expression, mouth closed in a small natural smile. Standing upright on her hind legs, bipedal, arms relaxed down at her sides — NOT a T-pose, NOT arms outstretched, NOT arms raised. Long thick tail clearly visible.

Panel layout, left to right, all three showing the same single character at identical scale, proportions and lighting: LEFT — full-body rear view, head to feet, back of the head, ears from behind, spine line and the full length of the tail visible. CENTER — full-body front view, head to feet, standing upright, arms relaxed at sides, feet flat and slightly apart, tail visible behind her silhouette. RIGHT — tight close-up portrait of her head and upper chest, looking straight into camera, face identical to the center panel.

Studio-grade 3D animation render, appealing modern feature-animation character language — NOT photoreal, NOT flat 2D cartoon, NOT a plush toy, NOT a clay or plasticine figure. Clean neutral mid-grey seamless background with no horizon line, no gradient and no vignette. Soft even shadowless illumination arriving from all directions, no key light, no rim light, no hard shadows on the character or the ground, no specular hotspots. Subtle soft contact shadow under each pose. Thin light divider lines between the three panels. Deep focus, whole figure sharp in every panel.

No clothing, no accessories, no props, no text, no letters, no numbers, no labels, no watermarks, no logos, no grid lines, no axis lines, no 3D cursor, no viewport overlay, no user interface elements, no measurement guides. Nothing in the frame except the three panels of the character on the grey background. 16:9.
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
