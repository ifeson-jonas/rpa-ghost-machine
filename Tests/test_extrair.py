
import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import extrair_dados_pdf

def test_extrair_dados_pdf():
    caminho_pdf = os.path.join(os.path.dirname(__file__), "../pdfs/boletoteste.pdf")
    dados = extrair_dados_pdf(caminho_pdf)

    assert dados["cnpj"] == "12.345.678/0001-99"
    assert "R$" in dados["valor"]
    assert "1.234,56" in dados["valor"]
    assert dados["vencimento"] == "15/09/2025"

