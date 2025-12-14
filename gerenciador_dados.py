import json
import os
from backending.FreteEcommerce import acumuladores

def carregar_dados(nome_arquivo):
    pasta = os.path.join("backending", "Dados")
    caminho_completo = os.path.join(pasta, nome_arquivo)
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    try:
        with open(caminho_completo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            acumuladores.update(dados)
    except FileNotFoundError:
        with open(caminho_completo, "w", encoding="utf-8") as f:
            json.dump(acumuladores, f, indent=4, ensure_ascii=False)


def salvar_dados(nome_arquivo, dados):
    pasta = os.path.join("backending", "Dados")
    caminho_completo = os.path.join(pasta, nome_arquivo)
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    with open(caminho_completo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
