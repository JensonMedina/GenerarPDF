from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generar_pdf(ruta_salida: str):
    pdf = canvas.Canvas(ruta_salida, pagesize=A4)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, 800, "PDF generado")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 770, "Contenido generado desde Python.")

    pdf.save()