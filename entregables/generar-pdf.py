# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                NextPageTemplate)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

VERDE   = colors.HexColor("#14432A")
VERDE2  = colors.HexColor("#2F6B47")
ORO     = colors.HexColor("#B08430")
TINTA   = colors.HexColor("#232323")
GRIS    = colors.HexColor("#6B6B6B")
CREMA   = colors.HexColor("#F7F5F0")
LINEA   = colors.HexColor("#D9D3C7")

W, H = A4
MX = 22*mm

def st(name, **kw):
    base = dict(fontName="Helvetica", fontSize=10, leading=14, textColor=TINTA)
    base.update(kw)
    return ParagraphStyle(name, **base)

S = {
 "kicker":  st("kicker", fontName="Helvetica-Bold", fontSize=8, leading=11,
               textColor=ORO, spaceAfter=3),
 "h1":      st("h1", fontName="Helvetica-Bold", fontSize=19, leading=23,
               textColor=VERDE, spaceAfter=2),
 "h2":      st("h2", fontName="Helvetica-Bold", fontSize=12.5, leading=16,
               textColor=VERDE, spaceBefore=11, spaceAfter=5),
 "sub":     st("sub", fontSize=9.5, leading=13, textColor=GRIS, spaceAfter=9),
 "body":    st("body", fontSize=10, leading=15, spaceAfter=6),
 "small":   st("small", fontSize=8.6, leading=12, textColor=GRIS),
 "esc":     st("esc", fontSize=9.2, leading=13, textColor=GRIS,
               fontName="Helvetica-Oblique", spaceAfter=8),
 "who":     st("who", fontName="Helvetica-Bold", fontSize=8.6, leading=12,
               textColor=VERDE2),
 "whoT":    st("whoT", fontName="Helvetica-Bold", fontSize=8.6, leading=12,
               textColor=ORO),
 "beat":    st("beat", fontName="Helvetica-Bold", fontSize=9.5, leading=16,
               textColor=colors.HexColor("#C9BEA6")),
 "line":    st("line", fontSize=11, leading=16, textColor=TINTA),
 "nota":    st("nota", fontSize=9, leading=13, spaceAfter=5,
               leftIndent=13, firstLineIndent=-13),
 "covT":    st("covT", fontName="Helvetica-Bold", fontSize=40, leading=42,
               textColor=colors.white, alignment=TA_LEFT),
 "covS":    st("covS", fontSize=13, leading=19, textColor=colors.HexColor("#CFE0D3")),
 "covK":    st("covK", fontName="Helvetica-Bold", fontSize=9, leading=12,
               textColor=ORO),
}

# ---------------------------------------------------------------- contenido
CAPS = [
{"n":"00","fac":"Capítulo de presentación","tit":"Hola, soy Tita",
 "esc":"Tita sola. Se presenta y abre la serie.","dur":"~26 s","pal":64,
 "dlg":[("TITA","¡Hola! Soy Tita. Comadreja, curiosa de oficio, y mascota de la Universidad El Bosque."),
        ("TITA","A mí no me contrataron. Me eligieron ustedes, en una votación, entre tres finalistas. Gané por preguntona."),
        ("TITA","Desde entonces me la paso metiendo la nariz donde se está aprendiendo algo: laboratorios, consultorios, aulas, ensayos."),
        ("TITA","Si ves una cola larga doblando la esquina, soy yo."),
        ("TITA","¿Nos vamos? El bosque es grande.")],
 "notas":["<b>«Me eligieron ustedes»</b> es la línea que carga el capítulo: va con peso, un punto más lenta. No es un dato, es la razón de ser del personaje.",
          "La enumeración de cuatro comas se dice sin correr.",
          "<b>«El bosque es grande»</b> cierra con silencio detrás. Nada después."],
 "prog":None},

{"n":"01","fac":"Facultad de Medicina","tit":"Tres formas de cuidar a alguien",
 "esc":"Tita frente a la puerta de la sala de simulación. Se asoma por la ventanilla y habla a cámara.","dur":"~20 s","pal":51,
 "dlg":[("TITA","Detrás de esta puerta hay una sala de simulación."),
        ("TITA","Acá se practica antes de tocar a un paciente. Y se entra desde los primeros semestres."),
        ("TITA","Medicina, Instrumentación Quirúrgica y Optometría. Tres formas de cuidar a alguien."),
        ("TITA","Ven a conocer la Facultad de Medicina. Trae las preguntas; las batas las ponemos nosotros.")],
 "notas":["<b>Este es el capítulo de prueba de la serie.</b> Junta los dos riesgos: una enumeración de nombres propios y un remate con punto y coma. Si Giselle aguanta este, aguanta la serie.",
          "«Medicina, Instrumentación Quirúrgica y Optometría» es el punto de quiebre: comas marcadas, sin correr.",
          "<b>«Tres formas de cuidar a alguien»</b> convierte la lista en una idea. Sin esa frase, la enumeración se queda en trámite.",
          "Si se graba en video: no aparece ningún paciente, ni de espaldas."],
 "prog":"Medicina · Instrumentación Quirúrgica · Optometría"},

{"n":"02","fac":"Facultad de Creación y Comunicación","tit":"Siete programas en un piso",
 "esc":"Un piso donde se oyen cosas distintas a la vez: música, una sierra, alguien ensayando en voz alta.","dur":"~24 s","pal":60,
 "dlg":[("TITA","Acá suena de todo al mismo tiempo. Y es a propósito: son siete programas en un mismo piso."),
        ("TITA","Arquitectura, Artes Plásticas, Arte Dramático, Diseño Industrial, Diseño de Comunicación, Creación Digital y Formación Musical."),
        ("TITA","Se prestan herramientas. Y se meten en los proyectos del otro."),
        ("TITA","Ven a conocer Creación y Comunicación. Se entra por un programa y se sale con siete.")],
 "notas":["<b>La lista de siete es la línea más difícil de la serie.</b> Va lenta, con coma marcada entre cada nombre y respiración antes de «Creación Digital».",
          "Si no cabe: cuatro programas en voz y los siete en texto en pantalla. No se acelera la voz — se oye.",
          "<b>«Y es a propósito»</b> convierte el ruido en argumento. Sin esa frase, la primera línea suena a queja."],
 "prog":"Arquitectura · Artes Plásticas · Arte Dramático · Diseño Industrial · Diseño de Comunicación · Creación Digital · Formación Musical"},

{"n":"03","fac":"Facultad de Odontología","tit":"Del modelo a la clínica",
 "esc":"Laboratorio de simulación. Filas de cabezas de práctica.","dur":"~22 s","pal":54,
 "dlg":[("TITA","Esto es un modelo. No un paciente."),
        ("TITA","Acá se practica hasta que la mano sale sola. Y después sí: pacientes de verdad, acompañados, en las clínicas de la Universidad."),
        ("TITA","Antes de lo que la gente cree."),
        ("TITA","Ven a conocer la Facultad de Odontología. Se entra a mirar y se termina con las manos puestas.")],
 "notas":["<b>«acompañados»</b> va entre pausas reales a lado y lado. Es la palabra que dice que nadie está solo frente a un paciente; si se pega a la frase, se pierde.",
          "«Esto es un modelo. No un paciente.» es una aclaración divertida, no una advertencia.",
          "«Antes de lo que la gente cree» va sola, con orgullo contenido."],
 "prog":"Odontología"},

{"n":"04","fac":"Facultad de Enfermería","tit":"Cabeza fría y manos firmes",
 "esc":"Sala de simulación, con un maniquí en la camilla.","dur":"~18 s","pal":45,
 "dlg":[("TITA","¿Qué se necesita para estudiar Enfermería? Cabeza fría y manos firmes."),
        ("TITA","Lo demás se aprende. Acá primero, en simulación. Después en hospitales, con pacientes de verdad."),
        ("TITA","Antes de lo que crees."),
        ("TITA","Ven a conocer la Facultad de Enfermería. Cuidar es una carrera, y empieza acá.")],
 "notas":["<b>Este capítulo es el termómetro de la voz.</b> «Cuidar es una carrera» es lo más cerca de lo institucional que llega la serie: si Giselle sonara demasiado infantil, se nota aquí primero. Grábalo temprano.",
          "Tita se hace la pregunta a sí misma y se la responde de una. No espera.",
          "«Lo demás se aprende» va suave y aparte. Es la que le abre la puerta a quien duda si puede."],
 "prog":"Enfermería"},

{"n":"05","fac":"Facultad de Psicología","tit":"No es solo escuchar",
 "esc":"Dos sillas frente a frente. Tita se sienta en una y habla a cámara.","dur":"~16 s","pal":41,
 "dlg":[("TITA","Psicología no es solo escuchar."),
        ("TITA","También es investigar, medir, y trabajar en colegios, empresas y clínicas."),
        ("TITA","Y sí, atender gente. En la práctica, siempre con supervisión."),
        ("TITA","Ven a conocer la Facultad de Psicología. Si te da curiosidad la gente, ya empezaste.")],
 "notas":["Tita desarma el prejuicio de entrada, sin pelear con nadie. Todo el capítulo cuelga de la primera frase.",
          "<b>«siempre con supervisión» no se recorta nunca</b>, aunque falte tiempo. Es la parte responsable de la respuesta.",
          "«colegios, empresas y clínicas» abre el campo laboral sin decir «campo laboral»."],
 "prog":"Psicología"},

{"n":"06","fac":"Facultad de Ciencias","tit":"Laboratorio, tablero y campo",
 "esc":"Mesón de laboratorio. Cajas de muestras rotuladas, botas de campo en el piso.","dur":"~20 s","pal":51,
 "dlg":[("TITA","Acá se estudia Biología, Matemática y Estadística."),
        ("TITA","Suena a laboratorio y tablero. Y lo es."),
        ("TITA","Pero también es campo: salir a tomar muestras fuera de Bogotá. Y los estudiantes van desde temprano."),
        ("TITA","Ven a conocer la Facultad de Ciencias. Si preguntar «por qué» te dura más de dos preguntas, es acá.")],
 "notas":["<b>«Y lo es»</b> es lo que hace creíble el giro: Tita no niega el prejuicio, lo completa.",
          "«Pero también es campo» sube. Es el giro del capítulo y desarma la idea de que ciencias es estar encerrada.",
          "«Estadística» es esdrújula y algunos motores la aplanan: escúchala."],
 "prog":"Biología · Matemática · Estadística"},

{"n":"07","fac":"Facultad de Ingeniería","tit":"Todavía",
 "esc":"Taller. Sobre la mesa, algo con cables que debería moverse.","dur":"~15 s","pal":38,
 "dlg":[("TITA","Cuatro ingenierías: Ambiental, de Sistemas, Electrónica e Industrial."),
        ("TITA","Acá se hacen cosas que no existían el semestre pasado."),
        ("TITA","Casi ninguna funciona a la primera… todavía."),
        ("TITA","Ven a conocer la Facultad de Ingeniería. Acá «todavía» es la palabra favorita.")],
 "notas":["<b>Todo el capítulo cuelga de cómo suene «…todavía».</b> La pausa antes es real y la palabra va tranquila, casi contenta. Si suena a excusa, se cae. Si suena a promesa, funciona.",
          "La enumeración va rápida y segura, como quien se la sabe de memoria."],
 "prog":"Ingeniería Ambiental · de Sistemas · Electrónica · Industrial"},

{"n":"08","fac":"Facultad de Ciencias Jurídicas y Políticas","tit":"El consultorio jurídico",
 "esc":"Entrada del consultorio jurídico. Sillas de espera.","dur":"~20 s","pal":50,
 "dlg":[("TITA","Acá se estudia Derecho y Ciencia Política."),
        ("TITA","Y acá hay un consultorio jurídico donde los estudiantes atienden gratis a quien no puede pagar un abogado."),
        ("TITA","Casos de verdad. Personas de verdad."),
        ("TITA","Ven a conocer la Facultad de Ciencias Jurídicas y Políticas. Acá la ley no solo se estudia: se ejerce.")],
 "notas":["El nombre completo de la Facultad es largo: <b>dilo entero y sin correr.</b> Es lo que la gente tiene que poder buscar después.",
          "«Casos de verdad. Personas de verdad.» — punto real en el medio, el peso en la segunda mitad.",
          "Si se graba en video: la sala de espera va vacía o con figurantes. No se filma a consultantes reales."],
 "prog":"Derecho · Ciencia Política"},

{"n":"09","fac":"Facultad de Ciencias Económicas y Administrativas","tit":"Detrás de cada cifra hay alguien",
 "esc":"Un salón con una hoja de cálculo proyectada. Tita mira la pantalla demasiado de cerca y se voltea a cámara.","dur":"~20 s","pal":50,
 "dlg":[("TITA","Administración de Empresas, y Negocios y Relaciones Internacionales."),
        ("TITA","Suena a vivir en una hoja de cálculo. Pero no."),
        ("TITA","Es decidir sin tener toda la información. Y se practica con casos reales. La hoja es solo la herramienta."),
        ("TITA","Ven a conocer Ciencias Económicas y Administrativas. Detrás de cada cifra hay alguien.")],
 "notas":["<b>Cuidado con la línea de los programas:</b> tiene dos «y» seguidas y se entiende mal si no se marca la coma. La pausa va antes del primer «y», no después.",
          "«Pero no.» necesita el silencio después. Es el giro.",
          "El remate va sin solemnidad, como quien dice una regla práctica."],
 "prog":"Administración de Empresas · Negocios y Relaciones Internacionales"},

{"n":"10","fac":"Facultad de Educación","tit":"Nadie termina de aprender a enseñar",
 "esc":"Un salón después de clase. Material recortado sobre el escritorio. Cierra la serie.","dur":"~17 s","pal":42,
 "dlg":[("TITA","Acá se forman los profesores."),
        ("TITA","Y también vuelven los que ya son profesores. Porque enseñar cambia cada año, y nadie termina de aprender a enseñar."),
        ("TITA","Ven a conocer la Facultad de Educación. Si alguna vez explicaste algo y te gustó, es acá.")],
 "notas":["<b>Cierra la serie entera.</b> La invitación deja de ser sobre una facultad y pasa a ser sobre quien está mirando.",
          "«Y también vuelven los que ya son profesores» es el dato que le habla al que ya trabaja y piensa en volver.",
          "«nadie termina de aprender a enseñar» va lenta y sin subrayar. Si se dice como frase de cartel, se cae.",
          "Único capítulo que no nombra programas: no se pudo verificar la oferta."],
 "prog":None},
]

# ---------------------------------------------------------------- páginas
def portada(c, doc):
    c.saveState()
    c.setFillColor(VERDE); c.rect(0, 0, W, H, fill=1, stroke=0)
    # marca de agua: silueta de cola
    c.setStrokeColor(colors.HexColor("#1B5335")); c.setLineWidth(46)
    c.setLineCap(1)
    p = c.beginPath(); p.moveTo(W-16*mm, 22*mm)
    p.curveTo(W+10*mm, 70*mm, W-64*mm, 74*mm, W-42*mm, 128*mm)
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()

def interior(c, doc):
    c.saveState()
    c.setFillColor(CREMA); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(VERDE); c.rect(0, H-9*mm, W, 9*mm, fill=1, stroke=0)
    c.setStrokeColor(LINEA); c.setLineWidth(0.5)
    c.line(MX, 16*mm, W-MX, 16*mm)
    c.setFont("Helvetica", 7.4); c.setFillColor(GRIS)
    c.drawString(MX, 11.5*mm, "Tita  ·  Serie de cortos  ·  Universidad El Bosque")
    c.drawRightString(W-MX, 11.5*mm, "%d" % (doc.page - 1))
    c.restoreState()

doc = BaseDocTemplate("/home/user/tita/entregables/tita-guiones.pdf",
        pagesize=A4, leftMargin=MX, rightMargin=MX,
        topMargin=20*mm, bottomMargin=22*mm,
        title="Tita — Serie de cortos · Guiones",
        author="Universidad El Bosque", subject="Guiones de la serie de cortos de Tita")

fr_cov = Frame(MX, 30*mm, W-2*MX, H-70*mm, id="cov",
               leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
fr_int = Frame(MX, 22*mm, W-2*MX, H-44*mm, id="int",
               leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([
    PageTemplate(id="portada", frames=[fr_cov], onPage=portada),
    PageTemplate(id="interior", frames=[fr_int], onPage=interior),
])

F = []
def P(txt, s): F.append(Paragraph(txt, S[s]))

# ---- portada
F.append(Spacer(1, 52*mm))
P("SERIE DE CORTOS", "covK")
F.append(Spacer(1, 5))
P("Tita", "covT")
F.append(Spacer(1, 5))
P("Once capítulos.<br/>Uno por facultad.", "covT")
F.append(Spacer(1, 12*mm))
P("Guiones completos, notas de locución y ficha de producción.<br/>"
  "Universidad El Bosque · 7 de septiembre de 2026", "covS")
F.append(Spacer(1, 8*mm))
t = Table([["Voz de Tita", "Giselle"],
           ["Método", "Doblaje sobre voz real · Tita sola"],
           ["Duración", "Máximo 30 segundos por capítulo"]],
          colWidths=[38*mm, 100*mm])
t.setStyle(TableStyle([
    ("FONT",(0,0),(0,-1),"Helvetica-Bold",8.4),
    ("FONT",(1,0),(1,-1),"Helvetica",8.4),
    ("TEXTCOLOR",(0,0),(0,-1),ORO),
    ("TEXTCOLOR",(1,0),(1,-1),colors.white),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),("TOPPADDING",(0,0),(-1,-1),4),
    ("LINEBEFORE",(0,0),(0,-1),1.2,ORO),
    ("LEFTPADDING",(0,0),(0,-1),8),
]))
F.append(t)
F.append(NextPageTemplate('interior'))
F.append(PageBreak())

# ---- página de contexto
def rule():
    tt = Table([[""]], colWidths=[W-2*MX], rowHeights=[1])
    tt.setStyle(TableStyle([("LINEBELOW",(0,0),(-1,-1),0.7,LINEA)]))
    F.append(Spacer(1,3)); F.append(tt); F.append(Spacer(1,7))

P("CÓMO SE LEE ESTE DOCUMENTO", "kicker")
P("La serie en una página", "h1")
rule()
P("Once capítulos cortos. El primero es la presentación de Tita; los diez siguientes "
  "invitan a conocer una facultad y sus programas. <b>Ninguno pasa de treinta segundos.</b>", "body")
P("<b>Habla Tita y nadie más.</b> No hay estudiantes, ni docentes, ni segundas voces: los "
  "once capítulos son ella sola frente a cámara.", "body")
P("Los diez de facultad tienen la misma forma, en cuatro tiempos: <b>dónde estamos</b>, "
  "<b>qué se estudia</b>, <b>el giro</b> —lo que uno no se esperaba de esa facultad— y "
  "<b>la invitación</b>, siempre con el nombre completo de la Facultad para que se pueda "
  "buscar después.", "body")

P("La voz", "h2")
P("Tita habla con la voz <b>Giselle</b>, del catálogo de presets de Higgsfield. "
  "No se clona ninguna voz de nadie: se elige una del catálogo. Giselle es la misma en los "
  "once capítulos — la voz es el personaje, y cambiarla entre capítulos rompe al personaje.", "body")

P("Cómo se graba", "h2")
P("<b>Se graba con voz real y a Tita se le pone la de Giselle encima.</b> La actuación —las "
  "pausas, la ironía, el «…Todavía»— la pone una persona; la herramienta solo cambia el timbre. "
  "Por eso el resultado no suena a locución sintética: no lo es del todo.", "body")
P("Como habla Tita sola, <b>es un video por capítulo y ya</b>: once tomas, once conversiones. "
  "Sin segundo actor, sin sincronizar pistas y sin riesgo de que dos voces se parezcan.", "body")

P("Cómo leer cada capítulo", "h2")
t = Table([
  [Paragraph("<b>Escena</b>", S["small"]), Paragraph("Dónde pasa. Sirve para el plano, no se dice en voz alta.", S["small"])],
  [Paragraph("<b>Guion</b>", S["small"]), Paragraph("Lo que dice Tita, literal. Cada bloque numerado es una respiración; los saltos entre bloques son pausas de verdad.", S["small"])],
  [Paragraph("<b>Notas</b>", S["small"]), Paragraph("Cómo se dice: dónde va la pausa, qué palabra lleva el peso, qué no se recorta.", S["small"])],
  [Paragraph("<b>Programas</b>", S["small"]), Paragraph("Los que nombra el capítulo. <b>Pendientes de verificar</b> — ver la última página.", S["small"])],
], colWidths=[26*mm, W-2*MX-26*mm])
t.setStyle(TableStyle([
  ("VALIGN",(0,0),(-1,-1),"TOP"),
  ("BOTTOMPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),6),
  ("LINEBELOW",(0,0),(-1,-2),0.4,LINEA),
  ("LEFTPADDING",(0,0),(0,-1),0),
]))
F.append(t)

P("El orden", "h2")
filas = [[Paragraph("<b>%s</b>" % c["n"], S["small"]),
          Paragraph("<b>%s</b>" % (c["fac"] if c["n"]!="00" else "Presentación"), S["small"]),
          Paragraph(c["tit"], S["small"]),
          Paragraph(c["dur"], S["small"])] for c in CAPS]
t = Table(filas, colWidths=[10*mm, 62*mm, 66*mm, 16*mm])
t.setStyle(TableStyle([
  ("VALIGN",(0,0),(-1,-1),"TOP"),
  ("BOTTOMPADDING",(0,0),(-1,-1),3.5),("TOPPADDING",(0,0),(-1,-1),3.5),
  ("LINEBELOW",(0,0),(-1,-2),0.3,LINEA),
  ("LEFTPADDING",(0,0),(0,-1),0),
  ("BACKGROUND",(0,1),(-1,2),colors.HexColor("#EDF2EC")),
  ("TEXTCOLOR",(3,0),(3,-1),GRIS),
]))
F.append(t)
F.append(Spacer(1,5))
P("Medicina abre y Creación y Comunicación sigue, por decisión de producción. "
  "Educación cierra.", "small")
F.append(PageBreak())

# ---- capítulos
for c in CAPS:
    P("CAPÍTULO %s%s" % (c["n"], "" if c["n"]=="00" else " · " + c["fac"].upper()), "kicker")
    P(c["tit"], "h1")
    P("%s&nbsp;&nbsp;·&nbsp;&nbsp;%s palabras" % (c["dur"], c["pal"]), "sub")
    rule()
    P("<i>%s</i>" % c["esc"], "esc")

    filas = []
    for i, (who, txt) in enumerate(c["dlg"], 1):
        filas.append([Paragraph("%d" % i, S["beat"]), Paragraph(txt, S["line"])])
    t = Table(filas, colWidths=[11*mm, W-2*MX-11*mm])
    t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),
        ("LEFTPADDING",(0,0),(0,-1),0),
        ("LEFTPADDING",(1,0),(1,-1),9),
        ("LINEBEFORE",(1,0),(1,-1),2,ORO),
        ("BACKGROUND",(0,0),(-1,-1),colors.white),
    ]))
    F.append(t)

    P("Notas de locución", "h2")
    for n in c["notas"]:
        P("<font color='#B08430'>—</font>&nbsp;&nbsp;%s" % n, "nota")

    if c["prog"]:
        F.append(Spacer(1,6))
        t = Table([[Paragraph("<b>PROGRAMAS QUE NOMBRA</b><br/><font size=9>%s</font>" % c["prog"],
                    ParagraphStyle("pr", fontName="Helvetica", fontSize=7.6, leading=11.5,
                                   textColor=VERDE))]],
                  colWidths=[W-2*MX])
        t.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#EDF2EC")),
            ("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9),
            ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
            ("LINEBEFORE",(0,0),(0,-1),2,VERDE2),
        ]))
        F.append(t)
    F.append(PageBreak())

# ---- página final
P("ANTES DE GRABAR", "kicker")
P("Lo que falta confirmar", "h1")
rule()
P("Cuatro cosas quedan abiertas. La primera es la que puede costar caro si se pasa por alto.", "body")

def bloque(titulo, cuerpo, tono=ORO):
    t = Table([[Paragraph("<b>%s</b><br/><br/>%s" % (titulo, cuerpo),
                ParagraphStyle("bq", fontName="Helvetica", fontSize=9.2, leading=13.5,
                               textColor=TINTA))]], colWidths=[W-2*MX])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),colors.white),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9),
        ("LINEBEFORE",(0,0),(0,-1),2.5,tono),
        ("BOX",(0,0),(-1,-1),0.4,LINEA),
    ]))
    F.append(t); F.append(Spacer(1,8))

bloque("1 · Los nombres de los programas",
 "Cada capítulo los nombra y <b>ninguno está verificado contra la página oficial de la "
 "Universidad</b>: salieron de resultados de búsqueda, porque el dominio estuvo bloqueado "
 "durante la redacción. Decir mal el nombre de un programa en una pieza institucional es el "
 "error que sí se nota, y el capítulo 02 nombra siete seguidos. Revísalos antes de grabar.")

bloque("2 · La prueba del primer capítulo",
 "Antes de grabar los once, se graba solo <b>Medicina</b> y se convierte la pista de Tita a "
 "Giselle. Se compara contra el original y se revisa: que la dicción no se embarre, que "
 "«Instrumentación Quirúrgica» sobreviva, que las pausas actuadas sigan ahí y que el acento "
 "no suene prestado.", VERDE2)

bloque("3 · Si Giselle aguanta lo institucional",
 "No se ha oído a Giselle diciendo una línea formal de la Universidad. El capítulo 04, "
 "Enfermería, es el mejor termómetro que hay en la serie: grábalo temprano.", VERDE2)

bloque("4 · Para qué piezas es la serie",
 "Reels, video institucional, señalética, audioguías. Cada destino pide algo distinto del "
 "montaje y del formato de salida.", VERDE2)

P("Una nota sobre el personaje", "h2")
P("Tita habla en <b>primera persona</b> en los once capítulos. Las publicaciones oficiales de "
  "la Universidad la narran en tercera. Es una decisión tomada a propósito: una mascota que "
  "invita funciona mejor hablando que siendo narrada. Conviene que quien apruebe la serie lo "
  "sepa, porque es visible desde la primera línea.", "body")

doc.build(F)
print("PDF listo")
