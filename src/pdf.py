import sys
from reportlab.lib.colors import pink, black, red, blue, green
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

def main(file_name, data):
    # canvas = Canvas("hello.pdf", pagesize=(612.0, 792.0))
    # canvas = Canvas("hello.pdf", pagesize=(8.5 * inch, 11 * inch))
    canvas = Canvas("font-colors.pdf", pagesize=LETTER)

    # Set font to Times New Roman with 12-point size
    canvas.setFont("Times-Roman", 12)

    canvas.setFillColor(blue)
    canvas.drawString(1 * inch, 10 * inch, "Blue text")
    canvas.setFillColor(red)
    canvas.drawString(1 * inch, 9.5 * inch, "red text")

    # Save the PDF file
    canvas.save()

    return(file_name, data)

if __name__ == "__main__":
    print(main(sys.argv[1:]))
