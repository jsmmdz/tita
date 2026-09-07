# Flujo — voz de Tita en Higgsfield

**Decisión (2026-08-31): no se clona ninguna voz.** Se elige una del catálogo
de presets de Higgsfield y se propone. Clonar exigiría una muestra real de
locución y resolver derechos sobre esa voz; con preset eso no aplica.

Los nombres entre `backticks` son las herramientas reales del MCP de
Higgsfield.

---

## Fase 1 — Investigar cómo habla la institución

Hecha. Está en `investigacion/lenguaje-institucional-ueb.md`.

Lo que salió y define todo lo demás: Tita es una **comadreja**, hembra,
elegida por votación de la comunidad, con atributos declarados de
**inteligencia, calidez, adaptabilidad, valentía y versatilidad**. Y la UEB
vive entre dos registros — el de la bioética y el de "mascoTITA" — así que la
voz tiene que aguantar los dos.

## Fase 2 — Escribir el texto de prueba

Hecha. Está en `prompts/texto-de-prueba.md`.

Un solo texto, siempre el mismo para todas las voces. Seis bloques, cada uno
midiendo algo distinto: primera impresión, frase larga, lista de atributos,
números y fechas, el lema institucional y el remate.

## Fase 3 — Audicionar

Hecha. Samuel preseleccionó seis a oído: **Kaia, Zoe, Luna, Chloe, Giselle y
Helena**. Están en `voces/finalistas.md` con su `voice_id`.

**El catálogo no dice idioma ni acento**, solo nombre y género. Un nombre en
español no garantiza que la voz hable español. Escuchar es el único método.

Criterios, en orden de peso:

1. ¿Aguanta el lema sin sonar a burla? — el que descarta.
2. ¿El acento es de Colombia, o suena prestado?
3. ¿Suena a estudiante o a comercial?
4. ¿Cómo pronuncia "31 de octubre de 2023" y "UEB"?

## Fase 3.5 — Elegir (hecha, 2026-09-07)

**La voz de Tita es Giselle** — `9d3128b8-dd25-5158-9bdb-2e69ac8998b9`.
Decisión de Samuel, tomada a oído sobre los previews, **sin correr la Ronda B**.

Eso cambia el resto del flujo:

- **La Ronda B queda cancelada.** Ya no hay seis voces que comparar.
- **La Ronda A sigue en pie y ahora se corre con Giselle**, no con Luna. Sirve
  para lo mismo que antes: decidir el motor. El motor no depende de la voz.
- Queda sin correr el **filtro de lema** sobre Giselle. Está anotado en
  `prompts/texto-de-prueba.md` y en `voces/finalistas.md`.

## Fase 4 — Escribir los guiones (hecha, 2026-09-07)

Están en `guiones/`. **Once capítulos**: uno por cada una de las diez
facultades, más el de presentación. **Habla Tita sola** — monólogo a cámara, de
**treinta segundos como techo**.

Los diez de facultad **invitan a conocer la facultad y sus programas**, en
cuatro tiempos: **el nombre de la facultad**, qué se estudia, el giro y la
invitación. Todos abren con "Esta es la Facultad de…". Orden
fijado por Samuel: **Medicina primero, Creación y Comunicación segundo**, y de
ahí para abajo los demás.

Que hable Tita sola simplifica la producción: **un video por capítulo**, once
tomas, once conversiones. Sin segundo actor y sin sincronizar pistas.

**Tita habla en primera persona.** Confirmado el 2026-09-07; el pendiente que
podía reescribir los once guiones queda cerrado.

Las reglas de escritura están en `guiones/README.md` y salen de la
investigación, no del gusto.

## Fase 4.5 — Probar el método

**Decidido el 2026-09-07: la serie se hace doblando voz real.** Se graba con
voz real y se le pone la de Giselle encima con `voice_change`. El motivo es la
expresividad: generar desde texto todavía suena robótico, y estos guiones viven
de las pausas y del tono.

**La Ronda A queda cancelada.** Por el camino del doblaje no hay motor que
elegir, así que no hay nada que comparar ni que gastar.

**La Prueba 1 es el capítulo `01-medicina`.** Procedimiento completo en
`guiones/PRUEBA-01.md`. En corto: se graba en video, se sube, se convierte con
Giselle, se compara contra el original.

Dos cosas que hay que saber:

- **`voice_change` recibe video, no audio.** Un `.wav` suelto no sirve de
  entrada. **El cuadro puede ir en negro total**: la herramienta no mira la
  imagen. Lo que devuelve también es video, así que hay que extraerle el audio.
- **`voice_change` no tiene parámetro de modelo.** Solo `video_id`, `voice_id`
  y `voice_type`. Así que la prueba no elige motor — no hay motor que elegir.
  Lo que decide es otra cosa, más de fondo: **si la serie se hace doblando voz
  real o generando desde texto.**

`generate_audio` queda como respaldo y solo si el doblaje falla después de
regrabar la toma. Ahí sí habría que correr la Ronda A: Giselle en los cuatro
motores, 2.20 créditos. **Qwen sigue descartado**, su interfaz no deja
seleccionar la voz.

## Fase 4.7 — Entregable

`entregables/tita-guiones.pdf` — los once guiones con notas de locución, ficha
de producción y los pendientes. Es el documento que se presenta.

Se regenera con `python3 entregables/generar-pdf.py`. **El script lee los `.md`
de `guiones/`**: no guarda el texto, lo saca de ahí. Cambias un guion, corres el
script, y el PDF queda al día. Los archivos de `guiones/` son la única fuente
de verdad.

Lo único que vive dentro del script es la tabla `TITULOS`: el título corto de
cada capítulo y la lista de programas que se muestra al pie. Si agregas un
capítulo, hay que agregarle su fila ahí.

## Fase 5 — Registrar y proponer

Cada tanda va a `registro/bitacora.md` con voz, parámetros y veredicto **por
bloque**, no un "quedó bien" general.

La propuesta final lleva: la voz elegida, dos alternativas, el audio de las
tres con el mismo texto, y el porqué contra los atributos declarados de Tita.

---

## Cuidado con los créditos

`generate_audio` cobra. El parámetro `use_unlim` decide si paga el saldo de
créditos o las generaciones ilimitadas de prueba. **Déjalo sin poner** salvo
que Samuel pida explícitamente usar las ilimitadas: así el servidor pregunta
antes de gastar en vez de decidir solo.

## Pendientes

- [ ] **Verificar los nombres de los programas** que se nombran en los guiones,
      contra `unbosque.edu.co`. Salieron de resultados de búsqueda. Es el
      pendiente más urgente: un nombre de programa mal dicho en pieza
      institucional sí se nota.
- [ ] Confirmar las citas de la investigación contra `unbosque.edu.co` — el
      dominio está bloqueado por el proxy de red de esta sesión.
- [ ] ¿Hay manual de marca de la UEB con tono de voz? Si existe, manda.
- [ ] ¿Para qué piezas es la voz — reels, video institucional, señalética?
- [ ] Revisar el Instagram de la UEB para el registro informal. No pude:
      el proxy bloquea el dominio.
- [ ] **Correr la Prueba 1** — grabar `01-medicina` en video y convertir la
      pista de Tita a Giselle. Ver `guiones/PRUEBA-01.md`. Es lo que desbloquea
      todo lo demás.
- [ ] Correr la Ronda A **solo si el doblaje falla después de regrabar**. Las
      Rondas A y B quedan canceladas por ahora: la voz está elegida y el método
      también.
- [ ] Correr el filtro de lema sobre Giselle: una línea suelta del lema, para
      saber si aguanta lo institucional.
