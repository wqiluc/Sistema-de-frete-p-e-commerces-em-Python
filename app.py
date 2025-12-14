from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from backending.FreteEcommerce import acumuladores
from backending.mensagens import rota_carregada
from backending.mensagens import resumo_log
from backending.gerenciador_dados import carregar_dados, salvar_dados

ARQUIVO_COMPRA = "compra_cliente.json"

app = Flask(__name__)


carregar_dados(ARQUIVO_COMPRA)

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def inicio():
    rota_carregada("INÍCIO")
    return render_template("index.html")


@app.route("/")
@app.route("/regioes")
@app.route("/regioes.html")
def regioes():
    rota_carregada("REGIÕES")
    return render_template("regioes.html")

@app.route("/")
@app.route("/exterior")
@app.route("/exterior.html")
def exterior():
    rota_carregada("EXTERIOR")
    return render_template("exterior.html")


@app.route("/")
@app.route("/preco")
@app.route("/preco.html")
def preco():
    rota_carregada("PREÇO")
    return render_template("preco.html")


@app.route("/")
@app.route("/peso")
@app.route("/peso.html")
def peso():
    rota_carregada("PESO")
    return render_template("peso.html")


@app.route("/")
@app.route("/resumo")
@app.route("/resumo.html")
def resumo():
    resumo_log()
    rota_carregada("RESUMO")

    total_dia = acumuladores["totalgeral"]
    quantidade = acumuladores["numerocompras"]

    return render_template("resumo.html", total_dia=total_dia, quantidade=quantidade)



salvar_dados(ARQUIVO_COMPRA, acumuladores)
