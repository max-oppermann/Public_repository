
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", "B", 16)
pdf.cell(0, 40, "CS50 Shirtificate", align='C')
pdf.image("shirtificate.png", 0, 50, 210)
name = input("Name:")
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 300, f"{name} took CS50", align='C')


pdf.output("shirtificate.pdf")

