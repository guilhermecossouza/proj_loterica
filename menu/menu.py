import servicos
import servicos.mega_sena
import servicos.menu


def get_opcoes_jogos():
    opcoes_menu = servicos.menu.get_nome_concursos()
    if opcoes_menu:
        qtd_opcoes = len(opcoes_menu)
        str_jogo = ""
        print("MENU")
        print("Escolha a opção desejada!\n")
        for chave, valor in enumerate(opcoes_menu):
            print(f" {chave + 1} - {valor.upper()}")
        while True:
            try:
                opcao = int(input("Informe a opção desejada: "))
                if 0 < opcao <= qtd_opcoes - 1:
                    str_jogo = opcoes_menu[opcao - 1]
                    break
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Opção inválida.")

        return str_jogo


def opcoes_informacao_jogo():
    print("Opções de informações do jogo escolhido:")
    opcoes_informacoes = ['RESULTADOS']
    qtd_opcoes = len(opcoes_informacoes)
    str_opcao = ""
    for chave, valor in enumerate(opcoes_informacoes):
        print(f"{chave + 1} - {valor}")

    while True:
        try:
            opcao = int(input("Informe a opção desejada: "))
            if 0 < opcao <= qtd_opcoes:
                str_opcao = opcoes_informacoes[opcao - 1]
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Opção inválida.")
    return str_opcao
