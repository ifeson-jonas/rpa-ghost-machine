from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
texto = """
CNPJ: 12.345.678/0001-99
Valor: R$ 1.234,56
Vencimento: 15/09/2025
"""
pdf.multi_cell(0, 10, texto)
pdf.output("pdfs/boletoteste.pdf")
print("PDF de teste criado em pdfs/boletoteste.pdf")

