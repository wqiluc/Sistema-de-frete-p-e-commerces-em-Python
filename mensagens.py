from backending.cores import VERDE, VERMELHO, AZUL, RESET

print(f"\n {VERDE}MENSAGENS.PY FOI IMPORTADO!\n {RESET}")

def rota_carregada(nome):
    print(f"{VERDE}[ROTA] {nome} carregada!{RESET}")

def erro_rota(nome):
    print(f"{VERMELHO}[ERRO] Falha ao carregar rota {nome}!{RESET}")

def resumo_log():
    print(f"{AZUL}[RESUMO] Rota de resumo carregada.{RESET}")
