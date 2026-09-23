"""Hoja de fórmulas de Física 1. Requiere: pip install reportlab."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
)

ROOT = Path(__file__).resolve().parent.parent

# Las únicas dependencias son ReportLab y una fuente DejaVu Sans del sistema.
FUENTES = (
    ROOT / "assets/fonts/DejaVuSans.ttf",
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    Path("/usr/local/share/fonts/DejaVuSans.ttf"),
)

# Títulos breves para ubicar rápidamente cada bloque de ecuaciones.
TITULOS = [
    "Desplazamiento y tiempo",
    "Pitágoras y trigonometría",
    "Componentes de vectores",
    "Velocidad y aceleración",
    "Movimiento rectilíneo uniforme",
    "Aceleración constante",
    "Desde el reposo",
    "Detención",
    "Caída libre (arriba positivo)",
    "Caída desde el reposo",
    "Lanzamiento vertical",
    "Caída libre (abajo positivo)",
    "Movimiento de proyectiles",
    "Lanzamiento horizontal",
]

GRUPOS = [
    [
        "Δx = x<sub>f</sub> − x<sub>i</sub>",
        "x<sub>f</sub> = x<sub>i</sub> + Δx",
        "x<sub>i</sub> = x<sub>f</sub> − Δx",
        "Δy = y<sub>f</sub> − y<sub>i</sub>",
        "Δt = t<sub>f</sub> − t<sub>i</sub>",
        "d = |Δx<sub>1</sub>| + |Δx<sub>2</sub>| + ⋯",
    ],
    [
        "h<super>2</super> = a<super>2</super> + b<super>2</super>",
        "h = √(a<super>2</super> + b<super>2</super>)",
        "a = √(h<super>2</super> − b<super>2</super>)",
        "b = √(h<super>2</super> − a<super>2</super>)",
        "sen θ = O/H",
        "cos θ = A/H",
        "tan θ = O/A = sen θ/cos θ",
        "O = H sen θ = A tan θ",
        "A = H cos θ = O/tan θ",
        "θ = arcsen(O/H) = arccos(A/H) = arctan(O/A)",
    ],
    [
        "A<sub>x</sub> = A cos θ",
        "A<sub>y</sub> = A sen θ",
        "A = √(A<sub>x</sub><super>2</super> + A<sub>y</sub><super>2</super>)",
        "|A<sub>x</sub>| = √(A<super>2</super> − A<sub>y</sub><super>2</super>)",
        "|A<sub>y</sub>| = √(A<super>2</super> − A<sub>x</sub><super>2</super>)",
        "A = A<sub>x</sub>/cos θ = A<sub>y</sub>/sen θ",
        "tan θ = A<sub>y</sub>/A<sub>x</sub>",
        "A<sub>y</sub> = A<sub>x</sub> tan θ",
        "A<sub>x</sub> = A<sub>y</sub>/tan θ",
        "|A<sub>x</sub>| = A sen φ",
        "|A<sub>y</sub>| = A cos φ",
        "R<sub>x</sub> = A<sub>x</sub> + B<sub>x</sub> + ⋯",
        "R<sub>y</sub> = A<sub>y</sub> + B<sub>y</sub> + ⋯",
        "R = √(R<sub>x</sub><super>2</super> + R<sub>y</sub><super>2</super>)",
    ],
    [
        "v<sub>med,x</sub> = Δx/Δt = (x<sub>f</sub> − x<sub>i</sub>)/(t<sub>f</sub> − t<sub>i</sub>)",
        "Δx = v<sub>med,x</sub> Δt",
        "Δt = Δx/v<sub>med,x</sub>",
        "r<sub>med</sub> = d<sub>total</sub>/Δt",
        "v<sub>x</sub> = dx/dt",
        "a<sub>med,x</sub> = Δv<sub>x</sub>/Δt = (v<sub>fx</sub> − v<sub>ix</sub>)/(t<sub>f</sub> − t<sub>i</sub>)",
        "Δv<sub>x</sub> = a<sub>med,x</sub> Δt",
        "v<sub>fx</sub> = v<sub>ix</sub> + a<sub>med,x</sub> Δt",
        "v<sub>ix</sub> = v<sub>fx</sub> − a<sub>med,x</sub> Δt",
        "Δt = Δv<sub>x</sub>/a<sub>med,x</sub>",
        "a<sub>x</sub> = dv<sub>x</sub>/dt = d<super>2</super>x/dt<super>2</super>",
    ],
    [
        "a = 0",
        "v = v<sub>0</sub> = Δx/t",
        "Δx = vt",
        "t = Δx/v",
        "x = x<sub>0</sub> + vt",
        "v = (x − x<sub>0</sub>)/t",
        "x<sub>0</sub> = x − vt",
    ],
    [
        "a = (v − v<sub>0</sub>)/t",
        "v = v<sub>0</sub> + at",
        "v<sub>0</sub> = v − at",
        "t = (v − v<sub>0</sub>)/a",
        "Δx = v<sub>0</sub>t + ½at<super>2</super>",
        "x = x<sub>0</sub> + v<sub>0</sub>t + ½at<super>2</super>",
        "v<sub>0</sub> = (Δx − ½at<super>2</super>)/t",
        "a = 2(Δx − v<sub>0</sub>t)/t<super>2</super>",
        "Δx = vt − ½at<super>2</super>",
        "v<super>2</super> = v<sub>0</sub><super>2</super> + 2aΔx",
        "Δx = (v<super>2</super> − v<sub>0</sub><super>2</super>)/(2a)",
        "a = (v<super>2</super> − v<sub>0</sub><super>2</super>)/(2Δx)",
        "v<sub>0</sub><super>2</super> = v<super>2</super> − 2aΔx",
        "v<sub>med</sub> = (v<sub>0</sub> + v)/2",
        "Δx = [(v<sub>0</sub> + v)/2]t",
        "t = 2Δx/(v<sub>0</sub> + v)",
        "v<sub>0</sub> = 2Δx/t − v",
        "v = 2Δx/t − v<sub>0</sub>",
        "t = [−v<sub>0</sub> ± √(v<sub>0</sub><super>2</super> + 2aΔx)]/a",
    ],
    [
        "v<sub>0</sub> = 0",
        "v = at",
        "Δx = ½at<super>2</super>",
        "v<super>2</super> = 2aΔx",
        "t = √(2Δx/a)",
    ],
    [
        "v = 0",
        "t<sub>det</sub> = −v<sub>0</sub>/a",
        "Δx<sub>det</sub> = −v<sub>0</sub><super>2</super>/(2a)",
    ],
    [
        "g ≈ 9,8 m/s<super>2</super>",
        "a<sub>y</sub> = −g",
        "v<sub>y</sub> = v<sub>0y</sub> − gt",
        "t = (v<sub>0y</sub> − v<sub>y</sub>)/g",
        "Δy = v<sub>0y</sub>t − ½gt<super>2</super>",
        "y = y<sub>0</sub> + v<sub>0y</sub>t − ½gt<super>2</super>",
        "v<sub>y</sub><super>2</super> = v<sub>0y</sub><super>2</super> − 2gΔy",
        "Δy = [(v<sub>0y</sub> + v<sub>y</sub>)/2]t",
    ],
    [
        "v<sub>0y</sub> = 0",
        "Δy = −½gt<super>2</super>",
        "v<sub>y</sub> = −gt",
        "h = ½gt<super>2</super>",
        "t = √(2h/g)",
        "|v<sub>y</sub>| = gt = √(2gh)",
    ],
    [
        "v<sub>y</sub> = 0",
        "t<sub>subida</sub> = v<sub>0y</sub>/g",
        "h<sub>máx</sub> = v<sub>0y</sub><super>2</super>/(2g)",
        "T<sub>misma altura</sub> = 2v<sub>0y</sub>/g = 2t<sub>subida</sub>",
        "v<sub>y,f</sub> = −v<sub>0y</sub>",
    ],
    [
        "a<sub>y</sub> = +g  (↓+)",
        "v<sub>y</sub> = v<sub>0y</sub> + gt  (↓+)",
        "Δy = v<sub>0y</sub>t + ½gt<super>2</super>  (↓+)",
    ],
    [
        "a<sub>x</sub> = 0",
        "a<sub>y</sub> = −g",
        "v<sub>0x</sub> = v<sub>0</sub> cos θ",
        "v<sub>0y</sub> = v<sub>0</sub> sen θ",
        "Δx = v<sub>0x</sub>t = (v<sub>0</sub> cos θ)t",
        "x = x<sub>0</sub> + (v<sub>0</sub> cos θ)t",
        "t = Δx/v<sub>0x</sub>",
        "Δy = v<sub>0y</sub>t − ½gt<super>2</super>",
        "y = y<sub>0</sub> + (v<sub>0</sub> sen θ)t − ½gt<super>2</super>",
        "v<sub>x</sub> = v<sub>0x</sub> = v<sub>0</sub> cos θ",
        "v<sub>y</sub> = v<sub>0y</sub> − gt = v<sub>0</sub> sen θ − gt",
        "v<sub>y</sub><super>2</super> = v<sub>0y</sub><super>2</super> − 2gΔy",
        "v = √(v<sub>x</sub><super>2</super> + v<sub>y</sub><super>2</super>)",
        "θ<sub>v</sub> = atan2(v<sub>y</sub>, v<sub>x</sub>)",
        "y − y<sub>0</sub> = (tan θ)(x − x<sub>0</sub>) − g(x − x<sub>0</sub>)<super>2</super>/(2v<sub>0</sub><super>2</super> cos<super>2</super> θ)",
        "t = [v<sub>0y</sub> ± √(v<sub>0y</sub><super>2</super> − 2gΔy)]/g",
        "v<sub>y,cima</sub> = 0",
        "t<sub>subida</sub> = v<sub>0y</sub>/g = v<sub>0</sub> sen θ/g",
        "H<sub>máx</sub> = v<sub>0y</sub><super>2</super>/(2g) = v<sub>0</sub><super>2</super> sen<super>2</super> θ/(2g)",
        "y<sub>máx</sub> = y<sub>0</sub> + H<sub>máx</sub>",
        "T<sub>misma altura</sub> = 2v<sub>0y</sub>/g = 2v<sub>0</sub> sen θ/g",
        "R<sub>misma altura</sub> = v<sub>0x</sub>T = v<sub>0</sub><super>2</super> sen(2θ)/g",
        "y<sub>f</sub> − y<sub>0</sub> = v<sub>0y</sub>T − ½gT<super>2</super>",
        "R = v<sub>0x</sub>T",
    ],
    [
        "v<sub>0y</sub> = 0",
        "Δx = v<sub>0x</sub>t",
        "Δy = −½gt<super>2</super>",
        "v<sub>x</sub> = v<sub>0x</sub>",
        "v<sub>y</sub> = −gt",
        "h = ½gt<super>2</super>",
        "t = √(2h/g)",
        "R = v<sub>0x</sub>√(2h/g)",
        "v<sub>0x</sub> = R/t = R√(g/(2h))",
        "|v<sub>y</sub>| = √(2gh)",
        "v<sub>impacto</sub> = √(v<sub>0x</sub><super>2</super> + 2gh)",
        "φ = arctan(|v<sub>y</sub>|/|v<sub>x</sub>|)",
    ],
]


def _registrar_fuente():
    if "FisicaDejaVu" in pdfmetrics.getRegisteredFontNames():
        return
    for ruta in FUENTES:
        if ruta.is_file():
            pdfmetrics.registerFont(TTFont("FisicaDejaVu", str(ruta)))
            return
    raise FileNotFoundError(
        "No se encontró DejaVuSans.ttf. Copialo a assets/fonts/DejaVuSans.ttf."
    )


def generar_pdf(ruta_salida="output/formulas-fisica.pdf"):
    """Genera el formulario A4. Acepta ruta absoluta o relativa a la raíz del proyecto."""
    _registrar_fuente()
    destino = Path(ruta_salida)
    if not destino.is_absolute():
        destino = ROOT / destino
    destino.parent.mkdir(parents=True, exist_ok=True)

    estilo = ParagraphStyle(
        "formula", fontName="FisicaDejaVu", fontSize=9.7,
        leading=16.2, textColor=colors.HexColor("#172536"), alignment=TA_LEFT,
        spaceAfter=1.8, splitLongWords=0,
    )

    estilo_titulo = ParagraphStyle(
        "titulo_seccion", parent=estilo, fontSize=10.4, leading=15,
        textColor=colors.HexColor("#17547A"), spaceAfter=0,
    )

    documento = BaseDocTemplate(
        str(destino), pagesize=A4, leftMargin=34, rightMargin=34,
        topMargin=32, bottomMargin=30, title="Fórmulas de Física 1",
        author="Jenson Medina",
    )
    ancho, alto = A4
    separacion = 22
    ancho_columna = (ancho - 68 - separacion) / 2
    marco_izquierdo = Frame(34, 30, ancho_columna, alto - 62,
                           leftPadding=3, rightPadding=3,
                           topPadding=2, bottomPadding=2)
    marco_derecho = Frame(34 + ancho_columna + separacion, 30,
                          ancho_columna, alto - 62,
                          leftPadding=3, rightPadding=3,
                          topPadding=2, bottomPadding=2)
    documento.addPageTemplates(PageTemplate(id="dos_columnas", frames=[marco_izquierdo, marco_derecho]))

    flujo = []
    assert len(TITULOS) == len(GRUPOS)
    for titulo, grupo in zip(TITULOS, GRUPOS):
        # El encabezado y la primera fórmula siempre quedan en la misma columna.
        flujo.append(KeepTogether([
            HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#B6C9D6")),
            Spacer(1, 6),
            Paragraph(titulo, estilo_titulo),
            Spacer(1, 4),
            Paragraph(grupo[0], estilo),
        ]))
        flujo.extend(Paragraph(expresion, estilo) for expresion in grupo[1:])
        flujo.append(Spacer(1, 7))
    documento.build(flujo)
    return destino


if __name__ == "__main__":
    generar_pdf()
