# Flujo visual — Tita en cuadro

> Este documento es el método **visual**. La voz va por su lado, en
> [`../FLUJO.md`](../FLUJO.md) y [`../guiones/PRUEBA-01.md`](../guiones/PRUEBA-01.md).
> Los guiones de [`../guiones/`](../guiones/) mandan sobre qué se dice; este
> documento define **cómo se ve Tita al decirlo**.

**Fuente del método:** el flujo de producción de *"El Día del Cartier"*
(`Flujo_Higgsfield_v1.md`) y el framework de
`Plan_Desarrollo_Metodologia_IA_v1.md`, ambos de Samuel. Lo que sigue es esa
metodología aterrizada a Tita — no reescrita, adaptada donde el caso lo obliga.

**Motores:** Seedance y Nano Banana Pro para generar. Después, Tita se guarda
como **elemento** para reusarla. Decidido por Samuel, 2026-09-08.

---

## Lo que cambia respecto del proyecto Cartier

Tres diferencias, y las tres van a favor.

### 1. El turnaround no se genera: se renderiza

En Cartier, `@sebastian` existía solo como fotos, así que **la hoja de
personaje era ella misma una generación** — con rondas de casting, riesgo de
deriva y una aprobación que costaba créditos.

Acá existe **la malla en Blender**. Las vistas salen de la cámara: exactas,
consistentes entre sí, gratis y repetibles. Se elimina el paso más caro y más
frágil del método original.

Consecuencia: **la hoja de personaje deja de ser algo que se genera y pasa a
ser algo que se colorea.** El modelo generativo no tiene que inventar la
geometría de Tita — ya se la damos resuelta. Solo tiene que ponerle color,
pelaje y luz encima de una forma que no está en discusión.

### 2. No hay marca ajena que proteger, pero sí institución

Cartier no tenía `@logo` que cuidar porque era contenido personal. Acá pasa lo
contrario: **es pieza institucional de la Universidad El Bosque.** Tita es
mascota oficial, elegida por votación de la comunidad. La deriva de personaje
no es un problema estético, es un problema de identidad de marca.

### 3. Once piezas, no una

Cartier es una pieza de 40s partida en cinco tomas. Acá son **once capítulos de
hasta 30s**, todos con el mismo personaje a cámara. Eso invierte el cálculo:
en Cartier el elemento se amortizaba en cinco tomas; acá se amortiza en once
capítulos. **Cada hora invertida en fijar el elemento se paga once veces.**
Y al revés: una Tita que derive entre capítulos rompe once piezas, no una.

---

## ⚠️ El riesgo central: forma y color vienen de fuentes distintas

Los renders del modelo son **gris arcilla, sin textura ni color**. El color
vive en las ilustraciones. Así que la hoja de personaje necesita dos fuentes —
y eso es exactamente lo que el flujo de Cartier advierte que no funciona:

> *"Mezclar referencias tampoco. Pedir «la forma de la 2 con la textura de la
> 1» da dos fuentes en conflicto y devuelve un promedio, no lo mejor de cada
> una."*

No es una advertencia teórica: ahí se perdió una hoja de personaje.

### Las tres salidas, en orden de preferencia

**A. Colorear en Blender antes de salir.** Si el modelo se puede texturizar y
renderizar ya con el color de Tita, el problema desaparece: hay **una sola
fuente**, y es exacta. Ninguna IA tiene que resolver el conflicto porque no
existe. Es más trabajo de tu lado y cero riesgo del lado generativo.
**Es la que recomiendo si el modelo está en condiciones de recibir material.**

**B. Roles explícitos en una sola pasada.** Si el coloreado en Blender no es
viable, se adjuntan las dos fuentes pero **con el rol de cada una escrito en el
prompt**, no dejado a interpretación: el render manda en geometría, silueta y
proporción; la ilustración manda **solo** en paleta y acabado. Y con el seguro
que ya usaste en Cartier: `do not redraw the geometry from memory`,
`the silhouette must not be reinterpreted`.

**C. Dos pasadas, nunca encadenadas.** Colorear el render primero, aprobar,
y recién ahí ajustar. Con la regla de Cartier intacta: **cada corrección sale
de la fuente limpia, nunca del resultado de la corrección anterior.**

> La regla de **no encadenar ediciones** se hereda tal cual. Si hay dos cosas
> que arreglar en la hoja de Tita, se arreglan en una sola pasada desde el
> render original. Escalar no recupera lo que se perdió, y lo que el modelo
> reinvente se vuelve canon en los once capítulos.

---

## Elementos `@` de la serie

Igual que en Cartier: se suben una vez y se adjuntan en cada toma que los
necesite, en vez de re-describirlos en texto. **Cada archivo se llama igual que
su elemento.**

| Elemento | Qué es | Fuente | Estado |
|---|---|---|---|
| `@tita` | **El elemento que sostiene la serie.** Hoja de personaje a color: frontal, ¾ y perfil, alineadas y con luz pareja | Renders de Blender + ilustraciones | ⬜ Pendiente — es el paso 1 |
| `@tita_cara` | Hoja de expresiones: neutra, sonrisa, complicidad, sorpresa | Se deriva de `@tita` una vez aprobada | ⬜ |
| `@tita_cuerpo` | Cuerpo entero con la cola. **La cola es la mitad del personaje** y en el T-pose frontal no se ve | Render lateral (ya existe) | ⬜ |

**Locaciones — una por capítulo.** Cada capítulo pasa en un sitio distinto y
nombrado: la sala de simulación en Medicina, el piso de los siete programas en
Creación y Comunicación, el consultorio jurídico en Jurídicas. Se tratan como
`@joyeria` y `@times_square` en Cartier: **se generan y se aprueban como
elemento antes de usarse en una toma.**

> ⚠️ **Y acá hay un pendiente que no es generativo:** las locaciones son
> espacios reales de la UEB. Si no hay fotos de referencia, el modelo se
> inventa un campus — y en pieza institucional eso se nota tanto como un
> nombre de programa mal dicho. Es el mismo error que la cocina de otro país
> en la hackathon, pero con un campus que la comunidad reconoce.
> **Hace falta decidir: ¿locaciones reales de la UEB, o un mundo propio de
> Tita, declaradamente ilustrado?** No es una decisión de producción, es de
> dirección de arte, y define todos los prompts de fondo.

### Soul no aplica acá — va como elemento

Tita **no es una persona**, y el entrenamiento de Soul es para identidad
humana. Para un personaje no-humano el camino correcto es guardarla como
**elemento**, que además es instantáneo, admite varios sujetos en cuadro y
funciona con Nano Banana Pro, Seedream y Seedance. Es lo que dijo Samuel y es
lo correcto por construcción, no por preferencia.

---

## Qué motor para qué

La tabla de Cartier se hereda entera, porque es aprendizaje de producción real:

| | **Nano Banana Pro** | **Seedream** |
|---|---|---|
| **Fuerte** | Reproduce fielmente los elementos adjuntos. Sostiene la estructura de hoja: alineación, escala y luz pareja entre vistas | No toca nada de lo que el prompt no menciona |
| **Falla** | — | **Reconstruye objetos de memoria** en vez de copiarlos del adjunto |

Aplicado a Tita:

- **La hoja de personaje `@tita`** → **Nano Banana Pro.** Entiende *model
  sheet* como documento técnico. Seedream lo lee como sesión de fotos y mueve
  cámara, luz y escala entre vistas — que es justo lo que una hoja no puede
  permitirse.
- **Ajustar un detalle sin tocar el resto** (el tono de un ojo, una oreja) →
  **Seedream.**
- **Las tomas de video** → **Seedance**, con `@tita` adjunta.

---

## ⚠️ El choque entre lo visual y la voz: el lip sync

Esto no está resuelto en ningún documento del repo y hay que decidirlo antes
de generar la primera toma.

Los once capítulos son **Tita hablando a cámara**. Y el método de voz ya
decidido es **doblaje con `voice_change` sobre voz real**. Pero:

> **`voice_change` no mira la imagen.** Solo reemplaza el audio y lo vuelve a
> pegar. No analiza labios, ni cara, ni sincroniza nada.

Es decir: si Tita mueve la boca en cuadro, **el movimiento no va a
corresponder con lo que se oye**, salvo que el video se genere ya sincronizado
contra el audio final. Y el audio final solo existe después de grabar y
convertir.

Tres caminos, y hay que elegir uno:

1. **Tita no habla en cuadro.** Es narradora en off y en imagen se la ve
   haciendo cosas: recorriendo la facultad, asomándose a la ventanilla de la
   sala de simulación —que es literalmente lo que dice la situación del
   capítulo 01—, señalando. **Elimina el problema entero** y es fiel a los
   guiones tal como están escritos.
2. **El audio primero, el video después.** Se graba, se convierte con Giselle,
   y ese audio final se usa como entrada de un modelo con lip sync. Invierte
   el orden de producción y ata cada toma a un audio ya cerrado: cualquier
   cambio de guion obliga a regenerar el video.
3. **Boca estilizada.** Tita habla pero sin articulación realista, al modo de
   mucha animación de mascota. Barato y honesto, pero hay que probar que no se
   lea como error.

**Recomiendo la 1**, y no por comodidad: los guiones ya están escritos como
monólogo con una situación física por capítulo. La 1 es la que respeta lo que
ya está aprobado en vez de obligar a reescribirlo.

---

## Orden de ejecución

Del tutorial y de Cartier: **todos los elementos existen antes de la primera
toma.**

| # | Paso | Motor | Estado |
|---|---|---|---|
| 0 | **Renders del modelo 3D** — frontal, ¾ y perfil. El ¾ es el que más ayuda y todavía no existe | Blender | ⬜ **← SIGUIENTE** |
| 0b | **Decidir el camino de color** — A, B o C de la sección de arriba | — | ⬜ |
| 1 | **`@tita`** — hoja de personaje a color | Nano Banana Pro | ⬜ |
| 2 | **`@tita_cara`** — hoja de expresiones | Nano Banana Pro | ⬜ |
| 3 | **Decidir el mundo de Tita** — campus real o ilustrado | — | ⬜ |
| 4 | **Locación del capítulo 01** — la sala de simulación | Nano Banana Pro | ⬜ |
| 5 | **Toma de prueba: capítulo 01** — Tita en la puerta de la sala | Seedance | ⬜ |
| 6 | Los otros diez capítulos | Seedance | ⬜ |

**El capítulo 01 es la toma de prueba visual**, por la misma razón que ya es la
prueba de voz: si Tita aguanta ahí, aguanta la serie. Es el equivalente de la
toma E del reloj en Cartier — la que decide si la pieza vale la pena.

---

## Presupuesto — a confirmar

Mismo pendiente que en Cartier, con la misma postura conservadora mientras no
se confirme: **720p generado + escalado ×2 en post, lote de 2.**

Falta confirmar con Samuel:

1. ¿720p + escalado, o hay margen para tirar directo más alto?
2. ¿Lote de 2 o de 4?
3. ¿El plan Ultra sigue vigente en esta cuenta?

Si aplica el criterio conservador, las consecuencias de diseño para Tita son
concretas: **el pelaje y los bigotes se piden en formas grandes y legibles**,
no en textura fina — es lo que peor sobrevive a 720p + ×2. Y los ojos, que son
el rasgo que más identifica a Tita, piden encuadre cerrado.

Y la regla de créditos del repo se mantiene: **`use_unlim` se deja sin poner**
salvo que Samuel pida explícitamente las ilimitadas, para que el servidor
pregunte antes de gastar.

---

## Qué falta decidir

1. **El camino de color** — A, B o C. Bloquea el paso 1.
2. **El mundo de Tita** — campus real de la UEB o ilustrado. Bloquea toda
   locación.
3. **El lip sync** — cuál de los tres caminos. Bloquea toda toma de video.
4. **Aspect ratio.** Los guiones apuntan a redes (reels), lo que sugiere 9:16,
   pero no está escrito en ningún lado del repo. En Cartier también quedó
   pendiente. Va en el prompt; la resolución y el lote no.
5. **Presupuesto** — ver arriba.

Nada de esto es generativo. Son decisiones de dirección de arte, y el flujo de
Cartier es claro en que van **antes** de escribir el primer prompt.
