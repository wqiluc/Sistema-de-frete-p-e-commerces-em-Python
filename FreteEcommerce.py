totalgeral = 0
numerocompras = 0

def menu_inicial():
    print(" \n=== Bem-vindo ao Sistema de Frete para E-commerce em Python ===")
    print("\nVocê informará:")
    print("- O preço do seu produto")
    print("- O peso do seu produto (em kg)")
    print("- A região de Entrega\n")
menu_inicial()

def menu_regioes_de_entrega():
    print("\n=== Regiões de Entrega Disponíveis ===")
    print("1 - Norte")
    print("2 - Nordeste")
    print("3 - Centro-Oeste")
    print("4 - Sudeste")
    print("5 - Sul\n")
menu_regioes_de_entrega

while True:
    precoproduto = input("Digite o preço do seu produto: R$ ")
    while True:
        try:
            precoproduto = float(precoproduto.replace(",", "."))
            if precoproduto <= 0:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido! Digite um preço real (apenas números).")
            precoproduto = input("Digite o preço do seu produto: R$ ")

    pesoproduto = input("Digite o peso do seu produto (em kg): ")
    while True:
        try:
            pesoproduto = float(pesoproduto.replace(",", "."))
            if pesoproduto <= 0:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido! Digite um peso real (apenas números).")
            pesoproduto = input("Digite o peso do seu produto (em kg): ")

    if pesoproduto <= 1.00:
        valorfrete = 15
    elif pesoproduto <= 5:
        valorfrete = 25
    else:
        valorfrete = 25 + ((pesoproduto - 5) * 5)

    regiao_entrega = input("Digite a região de entrega: ")
    while not regiao_entrega.isdigit() or regiao_entrega not in ["1", "2", "3", "4", "5"]:
        print("Região inválida. Selecione uma entre as 5 opções.")
        regiao_entrega = input("Digite a região de entrega: ")
    regiao_entrega = int(regiao_entrega)

    if regiao_entrega in [1, 2]:
        valorfrete += 10
        print("\nAdicional de R$10,00 aplicado (Norte/Nordeste)")
    else:
        print("\nRegião sem adicional de frete.")

    valortotalcompra = precoproduto + valorfrete
    numerocompras += 1
    totalgeral += valortotalcompra

    print(f"\nFrete total: R${valorfrete:.2f}")
    print(f"Valor total desta compra: R${valortotalcompra:.2f}")

    pergunta = input("\nDeseja continuar comprando? (S/N): ").strip().lower()
    while pergunta not in ["s", "n"]:
        print("Erro. Responda APENAS com S ou N.")
        pergunta = input("Deseja continuar comprando? (S/N): ").strip().lower()

    if pergunta == "s":
        print("\nContinuando a compra...\n")
        continue
    else:
        print("\nCompra Finalizada!! Confira seu extrato abaixo :)")
        print(f"\nTotal geral das suas compras: \033[1;34m R${totalgeral:.2f}")
        print(f"Você realizou: {numerocompras} compra(s)")

        if totalgeral > 200:
            valordesconto = totalgeral * 0.05
            valorfinal = totalgeral - valordesconto
            print("\n🎉 Parabéns! Sua compra ultrapassou R$200,00 e ganhou 5% de desconto!")
            print(f"\n Desconto: R${valordesconto:.2f}")
            print(f"Valor final com desconto: R${valorfinal:.2f}")
        else:
            print("Nenhum desconto aplicado (total menor que R$200,00).")

        print("\033[0;32m ")
        print("\n" + "="*45)
        print("Obrigado por comprar conosco!✅:)")
        print("="*45)
        print("\033[1;33m Acompanhe seu rastreio pelo app 🚚")
        break