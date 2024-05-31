from servicos import loterias_caixa


def menu_principal():
    print('-='*15)
    print("{:^30}".format("Sitema Loterias"))
    print("{:^30}".format("MENU"))
    print("Informe a opção desejada:")
    nome_jogos = loterias_caixa.get_nome_jogos_oferecidos()
    for opcao, nome in enumerate(nome_jogos):
        print(f"{opcao + 1} - {nome}")
    while True:
        try:
            opcao_desejada = int(input("Informe a sua opção: ")) - 1
            if 0 <= opcao_desejada <= len(nome_jogos) - 1:
                nome_opcao_desejada = nome_jogos[opcao_desejada]
                break
            else:
                print("\033[31mOpção informada inválida.\033[m")
        except:
            print("\033[31mOpção informada inválida.\033[m")
    return nome_opcao_desejada


def menu_informacoes_concurso(nome_concurso):
    lista_opcaoes = ["Último concurso",
                     "Consulta concurso", "Conferir dezenas"]
    print(f"Você escolheu o concurso {nome_concurso}")
    for posicao, opcao in enumerate(lista_opcaoes):
        print(f"{posicao + 1} - {opcao}")

    while True:
        try:
            oposicao_escolhida = int(input("Informe a opção desejada: "))
            if 0 < oposicao_escolhida <= len(lista_opcaoes):
                oposicao_escolhida -= 1
                return lista_opcaoes[oposicao_escolhida]
            else:
                print("\033[31mOpção informada inválida.\033[m")
        except:
            print("\033[31mOpção informada inválida.\033[m")
