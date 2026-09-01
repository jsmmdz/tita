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

## Fase 4 — Probar

**Samuel lanza a mano en la interfaz de Higgsfield.** El detalle está en
`investigacion/modelos-y-flujo.md`. En corto, dos rondas en vez de una:

- **Ronda A — el motor.** Una sola voz, los cuatro motores. 2.20 créditos.
  Decide cuál motor habla español decente antes de mirar voces.
- **Ronda B — la voz.** Las seis finalistas en el motor que ganó. Entre 1.8
  y 6.0 créditos según cuál sea.

Total: **entre 4.0 y 8.2 créditos**, 10 generaciones.

Se separa así porque son dos preguntas distintas y mezclarlas obliga a comparar
todo contra todo. **Qwen quedó descartado: su interfaz no deja seleccionar la
voz.** Quedan cuatro motores, de 0.30 a 1.0 crédito por línea. El default, Seed
Audio, es el más caro.

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

- [ ] Confirmar las citas de la investigación contra `unbosque.edu.co` — el
      dominio está bloqueado por el proxy de red de esta sesión.
- [ ] ¿Hay manual de marca de la UEB con tono de voz? Si existe, manda.
- [ ] ¿Tita habla en primera persona o alguien narra sobre ella? Lo oficial la
      narra en tercera. **Esto reescribe el texto de prueba entero.**
- [ ] ¿Para qué piezas es la voz — reels, video institucional, señalética?
- [ ] Revisar el Instagram de la UEB para el registro informal. No pude:
      el proxy bloquea el dominio.
- [ ] Correr la Ronda A y luego la Ronda B. Las lanza Samuel a mano.
