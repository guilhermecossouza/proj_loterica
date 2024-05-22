from servicos import loterias_caixa


def menu_principal():
    print('-='*15)
    print("{:^30}".format("Sitema Loterias"))
    print("{:^30}".format("MENU"))
    print("Informe a opção desejada:")
    nome_opcao_desejada = ""
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
