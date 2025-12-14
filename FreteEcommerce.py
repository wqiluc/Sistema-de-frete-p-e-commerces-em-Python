acumuladores = {
    "totalgeral": 0,
    "numerocompras": 0,
    "preco_produto": 0,
    "frete_final": 0,
    "total_compra": 0,
    "desconto": 0,
    "valorfinal_totalgeral": 0,}


def calcular_frete_por_peso(peso):
    if peso <= 1:
        return 15
    elif peso <= 5:
        return 25
    else:
        return 25 + ((peso - 5) * 5)


def adicional_por_regiao(regiao, frete):
    if regiao in [1, 2]:
        return frete + 10, "Adicional aplicado"
    return frete, "Sem adicional"


def calcular_total_compra(preco_produto, peso_produto, regiao):
    acumuladores["numerocompras"] += 1

    frete_base = calcular_frete_por_peso(peso_produto)
    frete_final, mensagem_regiao = adicional_por_regiao(regiao, frete_base)

    total_compra = preco_produto + frete_final

    acumuladores["totalgeral"] += total_compra

    desconto = 0
    valorfinal_totalgeral = acumuladores["totalgeral"]

    if acumuladores["totalgeral"] > 200:
        desconto = acumuladores["totalgeral"] * 0.05
        valorfinal_totalgeral = acumuladores["totalgeral"] - desconto

  
    acumuladores["preco_produto"] = preco_produto
    acumuladores["frete_final"] = frete_final
    acumuladores["total_compra"] = total_compra
    acumuladores["desconto"] = desconto
    acumuladores["valorfinal_totalgeral"] = valorfinal_totalgeral

    dados_compra = {
        "preco_produto": preco_produto,
        "peso_produto": peso_produto,
        "regiao": regiao,
        "frete_final": frete_final,
        "total_compra": total_compra,
        "desconto": desconto,
        "valorfinal_totalgeral": valorfinal_totalgeral,
        "mensagem_regiao": mensagem_regiao
    }

    return dados_compra
