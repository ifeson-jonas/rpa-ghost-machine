import os
import re
import sys
import pandas as pd
from pypdf import PdfReader

def extrair_dados_pdf(caminho_pdf):
    with open(caminho_pdf, "rb") as arquivo:
        leitor = PdfReader(arquivo)  # Corrigida a identação

        texto = ""
        for pagina in leitor.pages:
            texto += pagina.extract_text() or ""

    print("=== TEXTO EXTRAÍDO ===")
    print(texto)
    print("======================")

    cnpj = re.search(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", texto)
    valor = re.search(r"R\$ ?[\d\.,]+", texto)
    vencimento = re.search(r"\d{2}/\d{2}/\d{4}", texto)

    return {
        "arquivo": os.path.basename(caminho_pdf),
        "cnpj": cnpj.group() if cnpj else "",
        "valor": valor.group() if valor else "",
        "vencimento": vencimento.group() if vencimento else ""
    }

def listar_pdfs(diretorio):
    return [
        os.path.join(diretorio, arquivo)
        for arquivo in os.listdir(diretorio)
        if arquivo.lower().endswith(".pdf")
    ]

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <pasta_com_pdfs>")
        sys.exit(1)

    pasta_pdfs = sys.argv[1]
    if not os.path.isdir(pasta_pdfs):
        print(f"Erro: {pasta_pdfs} não é um diretório válido.")
        sys.exit(1)

    pdfs = listar_pdfs(pasta_pdfs)
    if not pdfs:
        print("Nenhum arquivo PDF encontrado na pasta.")
        sys.exit(0)

    dados_extraidos = []
    for pdf in pdfs:
        try:
            dados = extrair_dados_pdf(pdf)
            dados_extraidos.append(dados)
        except Exception as e:
            print(f"Erro ao processar {pdf}: {e}")

    df = pd.DataFrame(dados_extraidos)
    df.to_csv("boletos_extraidos.csv", index=False)
    print("Boletos extraídos com sucesso!")

if __name__ == "__main__":
    main()

