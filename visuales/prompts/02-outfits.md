# Outfits de Tita

Variantes de vestuario sobre `@tita`. **Cada una es una edición de la hoja de
personaje, no un personaje nuevo** — es como el tutorial hace la versión de
incógnito de su protagonista `[06:05]`: misma hoja, mismo fondo, misma luz,
mismos paneles, y se cambia solo el vestuario. Eso es lo que mantiene la
geometría idéntica entre outfits.

## El elemento base

| Dato | Valor |
|---|---|
| Nombre | `TITA` |
| `element_id` | `7189d8d4-c405-4a57-a505-7852b5099154` |
| Categoría | `character` |
| Origen | Job `9aee2abf-0ecf-4b29-b5e6-ede75207c2f1` — variante B de Nano, ronda 2, cola corta |

**Cómo se usa:** se embebe `<<<7189d8d4-c405-4a57-a505-7852b5099154>>>` dentro
del texto del prompt. El backend inyecta la imagen y lo reescribe a `@TITA`.

> ⚠️ **`seedream_v5_pro` NO acepta Elements.** Los modelos que sí:
> `nano_banana_pro`, `nano_banana_2`, `gpt_image_2`, `seedream_v4_5`,
> `seedream_v5_lite`, `cinematic_studio_2_5`. El Seedream que veníamos usando
> para la comparación queda fuera del flujo de outfits.

## Por qué Nano Banana Pro y no Seedream

El tutorial dice que Seedream es lo mejor para vestuario `[03:32]`, pero
también que al editar **Nano conserva mejor la cara y Seedream mejor la tela**
`[06:33]`. Acá lo que no se puede perder es Tita, no el terciopelo. Y Seedream
5.0 Pro ni siquiera es opción por lo de arriba.

## La regla de color que gobierna estos outfits

**Tita es verde bosque muy oscuro.** Eso decide qué funciona:

- **El rojo navideño funciona solo.** Rojo sobre verde oscuro es la paleta
  navideña; no hay que forzar nada.
- **El negro de Halloween se funde.** Contra un pelaje casi negro, el negro
  desaparece y la silueta se vuelve una mancha. Por eso **el naranja hace todo
  el trabajo**: cada borde negro lleva ribete naranja, y el forro de la capa es
  naranja entero.

## Los tres outfits

### Navidad — traje completo de Santa

Elegido por Samuel sobre la opción de solo accesorios. **Costo asumido:** la
chaqueta tapa el panel crema del pecho, que es la mitad de la silueta de Tita.
Mitigación dentro del prompt: cara, orejas, bigotes, patas rosadas y cola
quedan descubiertos, y la cabeza sigue siendo un tercio de la altura — que es
donde vive la identidad.

```text
Edit the attached three-panel character reference sheet of <<<7189d8d4-c405-4a57-a505-7852b5099154>>>. Keep everything about her identical: the same three panels in the same order, the same body proportions, the same large head, the same face, the same emerald-green eyes, the same cream muzzle, the same pink nose and paws, the same short low tail, the same grey seamless background, the same soft shadowless studio lighting and the same camera framing. Change exactly one thing: she is now dressed as Santa Claus. Outfit, applied consistently in all three panels: a rich crimson-red velvet Santa jacket, cut short and tailored to her round pear-shaped body, with thick soft white plush trim at the collar, cuffs and hem; a wide black leather belt with a large square gold buckle at her waist; matching crimson-red velvet trousers with white plush cuffs, ending above her ankles; and a crimson-red Santa hat with a white plush band and a big white pompom, flopping softly to one side over one ear. Her feet stay bare pink paws, no boots. Her face, ears, whiskers and tail remain completely uncovered and unchanged. The red velvet reads as large soft shapes with gentle sheen. Warm friendly expression, mouth closed in a small natural smile, arms relaxed at her sides. Studio-grade 3D animation render, appealing feature-animation quality, 4K. No text, no logos, no props, one character only.
```

### Halloween — bruja

Sombrero puntudo y capa corta. La silueta del sombrero se lee en miniatura, y
el ribete naranja evita que el negro se coma el contorno.

```text
Edit the attached three-panel character reference sheet of <<<7189d8d4-c405-4a57-a505-7852b5099154>>>. Keep everything about her identical: the same three panels in the same order, the same body proportions, the same large head, the same face, the same emerald-green eyes, the same cream muzzle, the same pink nose and paws, the same short low tail, the same grey seamless background, the same soft shadowless studio lighting and the same camera framing. Change exactly one thing: she is now dressed as a friendly cartoon witch. Outfit, applied consistently in all three panels: a tall pointed witch hat with a wide floppy brim, its crown bending forward at the tip, black with a broad bright pumpkin-orange band around the base and an orange edge along the brim, sitting between her ears; and a short black cape reaching to her waist, fastened at the throat with a round orange clasp, its whole inner lining bright pumpkin orange so the orange is always visible where the cape opens and where the edges turn. Every edge of the black cape and hat carries a clear orange trim line, so the black never merges with her dark green fur. Her cream belly panel stays visible below the short cape. Her face, ears, whiskers and tail remain completely uncovered and unchanged. Cheerful and playful, not scary, mouth closed in a small natural smile, arms relaxed at her sides. Studio-grade 3D animation render, appealing feature-animation quality, 4K. No text, no logos, no broom, no props, one character only.
```

### Halloween — calabaza

Máximo contraste contra el verde. Tapa el torso, pero deja fuera la cabeza
entera, los brazos, las piernas y la cola. **Sin cara tallada:** una calabaza
con ojos compite con la cara de Tita y el cuadro queda con dos caras.

```text
Edit the attached three-panel character reference sheet of <<<7189d8d4-c405-4a57-a505-7852b5099154>>>. Keep everything about her identical: the same three panels in the same order, the same large head, the same face, the same emerald-green eyes, the same cream muzzle, the same pink nose, the same grey seamless background, the same soft shadowless studio lighting and the same camera framing. Change exactly one thing: her body is now inside a padded pumpkin costume. The costume is a big round soft pumpkin shell in bright saturated orange, with gentle vertical ribbing running from top to bottom, worn over her torso from just under her chin down to her hips, so it reads as a plump round pumpkin body. A short stubby curled green stem and one small green leaf sit at the top of the shell, just below her chin. Her arms and legs come out of the shell and stay her own deep forest green fur, her paws stay pink, and her short low tail stays visible below the shell at the back. Her whole head, face, ears and whiskers stay completely uncovered and unchanged above the costume, and the orange shell contrasts strongly against her dark green fur. Cheerful and playful, not scary, mouth closed in a small natural smile, arms relaxed at her sides. Studio-grade 3D animation render, appealing feature-animation quality, 4K. No text, no logos, no carved face on the pumpkin, no jack-o-lantern features, no props, one character only.
```

## Lección aplicada: prompts cortos

La ronda 2 de la hoja de personaje salió peor que la 1, y la causa probable
fue **exceso de negativos**: seis menciones en negativo de la cola y cuatro
formas de decir "sin logo". Nombrar algo en negativo hace que el modelo le
preste atención igual, y el prompt creció tanto que el bloque de paneles quedó
al final, donde pesa menos.

Estos tres prompts van a la inversa: **descripción positiva, un solo renglón de
negativos al cierre.** Es la densidad que usan los prompts del tutorial.

## Después de generar

1. **Batear y cosechar.** Dos variantes por outfit; una de cada cuatro sirve
   `[14:34]`.
2. **Verificar que la cara no derivó.** Es lo único que no se puede perder: si
   la Tita del outfit no es la misma Tita, el outfit no sirve.
3. **Subir la aprobada como su propio elemento** — `TITA-navidad`,
   `TITA-bruja`, `TITA-calabaza` — para poder invocarla igual que `@TITA`.
4. **Fila en `../../registro/bitacora.md`.**


---

# Segunda tanda — diseños con criterio

Los tres primeros (Santa, bruja, calabaza) son los obvios. Funcionan, pero
**no dicen nada sobre Tita ni sobre El Bosque**: cualquier mascota podría
llevarlos. Estos cuatro salen de algo.

Corridos en `seedream_v5_pro`, `2k`, 16:9, `count: 2`, con el job `9aee2abf`
como referencia directa.

| Diseño | Jobs |
|---|---|
| Navidad · verde y oro | `0590f53f-faec-468d-bd21-09930401f188` · `4d3779a7-daba-415c-b00a-e08ea2a7c10b` |
| Navidad · ruana | `f551e529-c58a-4235-b6a6-7a773ca98ca1` · `0287a0ed-36b7-42ea-b3d0-21ac6cf90db6` |
| Halloween · fantasma | `aa4c06cd-c6b5-4ca0-a988-4199d2a2e765` · `2909a611-9c52-4d20-a328-4a0b9d0848ac` |
| Halloween · científica | `72940b75-408d-46b8-9ab6-3921aa720ecf` · `bf83afce-ba5a-4ada-ad68-cc6acf6cb5e2` |

## La idea detrás de cada uno

**Navidad · verde y oro.** El rojo de Santa pelea con el pelaje de Tita. La
salida no es pelearlo mejor: es **hacer la Navidad con su propio color.** Capa
de terciopelo verde más oscuro y saturado que su pelaje —para que se separe—,
forro y ribete dorados, broche de estrella, corona de pino con bayas rojas
mínimas. El verde deja de ser el problema y pasa a ser el concepto.

**Navidad · ruana.** El Bosque está en Bogotá y en diciembre hace frío. Una
ruana de lana crema con franjas roja y verde, en vez de un traje del Polo
Norte. **El crema sale del panel del pecho de Tita**, así que el outfit nace de
la paleta del personaje y no de fuera. Es el más local de los cuatro.

**Halloween · fantasma de sábana.** Sábana crema en pliegues grandes, dos
huecos, y por ahí salen sus ojos verdes. Tres cosas a favor: se lee en
miniatura —*"the tighter the frame, the less slop"* `[21:00]` premia las formas
grandes—, **resuelve solo el choque de negro contra verde** porque no hay
negro, y es el que mejor aguanta el escalado.

**Halloween · científica.** Bata blanca, gafas en la frente, pelaje alborotado,
tizne en la mejilla. **Es Halloween que además habla de la universidad** —
Medicina, Odontología, Ciencias, los laboratorios que los guiones ya nombran.
Un disfraz de bruja no dice nada de El Bosque; este sí. Sin matraz ni props: el
personaje solo, para que sirva como elemento.

## Qué mirar

Los dos primeros piden **tela**: terciopelo, dorado, lana gruesa. Es justo
donde Seedream debería ganarle a Nano `[06:33]`.

El fantasma es **el más riesgoso para la identidad**: le tapa la cara y deja
solo los ojos. Si los ojos no salen exactamente los de Tita, no hay nada más
que la identifique.


---

# Tercera tanda — cobertura completa

Samuel pidió **que los disfraces cubran más**. Dos soluciones distintas según
el disfraz:

- **Pijama con capucha** (reno, muñeco de nieve): el traje la cubre de pies a
  cabeza y la cabeza del personaje va en la capucha; **su cara real asoma por
  la abertura** y es lo único de pelaje verde que queda visible.
- **Cara descubierta, cuerpo tapado** (Frankenstein, Drácula): porque en esos
  dos la cara *es* el chiste. Frankenstein aprovecha que **el monstruo es verde
  y ella ya es verde** — su pelaje pasa a ser la piel. Drácula aprovecha que
  **los colmillos ya los tiene**.

Corridos en `seedream_v5_pro`, 16:9, `count: 2`, referencia `9aee2abf`.
**A 2K por error** — Samuel corrigió después que Seedream va a 1.5K.

| Disfraz | Jobs |
|---|---|
| Reno | `4b7cfb3e-c959-4fad-8eab-385cdaa00a49` · `3bd7441b-0b40-47f1-af56-634ec51b4044` |
| Muñeco de nieve | `d7631d15-4e43-4467-894f-a970366b2ba8` · `621c54d9-2532-496f-badc-af4032c5fe9d` |
| Frankenstein | `9128c3bf-6d74-45c6-a7c4-940563afc8c0` · `67545120-06a1-45b6-8c63-515cc7d610dc` |
| Drácula | `64d8c475-05e7-4df1-9c4c-3ca3986fa55d` · `dd2eaeae-b4ed-4f10-ba99-106730b8237a` |

**Riesgos anotados:** el muñeco de nieve es blanco sobre fondo gris claro y
puede perder la silueta contra el fondo. Frankenstein puede quedar todo en
valores bajos —chaqueta negra, camisa gris, pelaje verde oscuro—; si sale como
mancha, el arreglo es **subir la camisa a gris claro, no aclarar la chaqueta**.

---

# Cuarta tanda — cerrando temporadas y abriendo el calendario

Halloween y Navidad son dos fechas. El calendario de una universidad tiene
más, y esas piezas se usan más veces al año que los disfraces de temporada.

Corridos en `seedream_v5_pro`, **`1.5k`**, 16:9, `count: 2`, referencia
`9aee2abf`.

| Disfraz | Fecha | Jobs |
|---|---|---|
| Momia | Halloween | `9394780c-ca2e-4001-a38d-8cc190285b7a` · `d48230e3-3679-4c7b-b109-484a64c1b67f` |
| Esqueleto | Halloween | `551f7382-483f-47c0-9321-747975203613` · `802a5b34-a68c-4e4a-9fc0-658ccd02c4e3` |
| Duende | Navidad | `cc782b95-9d9d-477a-83bf-49fe86d50e26` · `f34abe04-321e-4dfe-a755-7d96f164fc08` |
| Grado — toga y birrete | Grados | `dd99f49f-2450-45ee-92eb-d8bcac9c00cc` · `1cd4d2f9-eb84-41ab-9765-b0569892b653` |
| Ángel del pesebre | Novena | `149b1a50-5fcc-48c4-923b-1632ca2ce300` · `3b89632f-e487-4a13-b334-3296b7c1aa00` |
| Cupido | Amor y Amistad | `3f6abef3-ba38-4401-9141-7a383deddf9b` · `8ccd1363-3a50-4a65-91d8-cc3a1d0bfade` |
| Estudiante | Bienvenida | `3a621219-be50-4be2-8a1d-dc7489a4bcbf` · `03f38b07-e451-4cb6-a0f5-bb7552e78fe1` |

**Excluidos por decisión de Samuel:** ambientalista y deportista.

## Tres decisiones de esta tanda

**El ángel del pesebre no es un disfraz obvio.** "Novena" es una tradición, no
una prenda; la figura vestible más legible del pesebre es el ángel. Si la pieza
de diciembre no debe llevar carga religiosa, **la ruana y el duende ya cubren
esa fecha** sin problema.

**Cupido va sin arco ni flecha.** Los props quedan fuera de las hojas de
personaje: si la hoja lleva un objeto, el objeto se vuelve parte del elemento y
reaparece en todas las generaciones posteriores.

**Grado y estudiante van sin nada escrito.** La toga lleva una estola verde y
blanca genérica, y el carnet del estudiante sale **en blanco a propósito**. Los
colores institucionales reales y el logo van en edición — misma decisión que se
tomó con el logo de la cola: la identidad de la UEB no se inventa.

---

# El guardarropa completo

Dieciocho outfits generados el 2026-09-08.

| Temporada | Outfits |
|---|---|
| **Halloween** (6) | bruja · calabaza · fantasma · científica · Frankenstein · Drácula · momia · esqueleto |
| **Navidad** (7) | Santa · verde y oro · ruana · reno · muñeco de nieve · duende · ángel del pesebre |
| **Calendario UEB** (3) | grado · Cupido · estudiante |

**Pendiente en todos:** ninguno se ha revisado. Falta elegir la variante buena
de cada pareja, verificar que la cara no derivó respecto de `@TITA`, y subir la
aprobada como su propio elemento. **Un outfit sin revisar no es un asset.**
