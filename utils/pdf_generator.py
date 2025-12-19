from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(text, filename="agentic_report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 40
    for line in text.split("\n"):
        c.drawString(40, y, line[:90])
        y -= 14
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
    return filename
