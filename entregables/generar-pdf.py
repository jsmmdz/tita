# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                NextPageTemplate)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import re

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
# ------------------------------------------------- los guiones, leidos de guiones/
# Fuente unica de verdad: los .md de guiones/. Este script no guarda el texto.
import os, glob as _glob
GDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "guiones")

TITULOS = {
 "00": ("Capítulo de presentación", "Hola, soy Tita", None),
 "01": (None, "Tres formas de cuidar a alguien",
        "Medicina · Instrumentación Quirúrgica · Optometría"),
 "02": (None, "Siete programas en un piso",
        "Arquitectura · Artes Plásticas · Arte Dramático · Diseño Industrial · "
        "Diseño de Comunicación · Creación Digital · Formación Musical"),
 "03": (None, "Del modelo a la clínica", "Odontología"),
 "04": (None, "Cabeza fría y manos firmes", "Enfermería"),
 "05": (None, "No es solo escuchar", "Psicología"),
 "06": (None, "Laboratorio, tablero y campo", "Biología · Matemática · Estadística"),
 "07": (None, "Todavía",
        "Ingeniería Ambiental · de Sistemas · Electrónica · Industrial"),
 "08": (None, "El consultorio jurídico", "Derecho · Ciencia Política"),
 "09": (None, "Detrás de cada cifra hay alguien",
        "Administración de Empresas · Negocios y Relaciones Internacionales"),
 "10": (None, "Nadie termina de aprender a enseñar", None),
}

def _md2rl(s):
    """Negrita de markdown a la etiqueta de reportlab, y comillas tipograficas."""
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r"<b>\1</b>", s)
    out, abierta = [], False
    for ch in s:
        if ch == '"':
            out.append("»" if abierta else "«"); abierta = not abierta
        else:
            out.append(ch)
    return "".join(out)

def _leer(path):
    raw = open(path, encoding="utf-8").read()
    n = re.match(r"# (\d\d) — (.+)", raw).groups()
    num, fac = n[0], n[1]
    dur = re.search(r"\| Duración estimada \| (~\d+ s) \|", raw).group(1)
    esc = re.search(r"\*\*Situación:\*\* (.+?)\n\n", raw, re.S)
    esc = " ".join(esc.group(1).split()) if esc else ""
    if esc: esc = esc[0].upper() + esc[1:]
    if not esc:
        m = re.search(r"^\*\*(?:Es el capítulo cero|Abre|Cierra).*?\*\*(.*?)\n\n", raw, re.S|re.M)
    guion = re.search(r"## Guion\n\n(.*?)\n\n## ", raw, re.S).group(1)
    bloques, cur = [], []
    for ln in guion.splitlines():
        ln = ln.lstrip(">").strip()
        ln = re.sub(r"^\*\*TITA:\*\*\s*", "", ln)
        if not ln:
            if cur: bloques.append(" ".join(cur)); cur = []
        else:
            cur.append(ln)
    if cur: bloques.append(" ".join(cur))
    notas_raw = re.search(r"## Notas de locución\n\n(.*?)(?:\n## |\Z)", raw, re.S).group(1)
    notas, cur = [], []
    for ln in notas_raw.splitlines():
        if ln.startswith("- "):
            if cur: notas.append(" ".join(cur))
            cur = [ln[2:].strip()]
        elif ln.strip() and cur:
            cur.append(ln.strip())
    if cur: notas.append(" ".join(cur))
    pal = sum(len([w for w in re.split(r"\s+", b) if re.search(r"\w", w)]) for b in bloques)
    fac0, tit, prog = TITULOS[num]
    return {"n": num, "fac": fac0 or fac, "tit": tit, "esc": esc, "dur": dur,
            "pal": pal, "dlg": [("TITA", _md2rl(b)) for b in bloques],
            "notas": [_md2rl(x) for x in notas], "prog": prog}

CAPS = [_leer(f) for f in sorted(_glob.glob(os.path.join(GDIR, "[0-9][0-9]-*.md")))]
assert len(CAPS) == 11, "esperaba once guiones, encontre %d" % len(CAPS)
for _c in CAPS:
    assert _c["dlg"], "guion vacio en %s" % _c["n"]

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
