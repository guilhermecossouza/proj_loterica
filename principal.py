from menu import menu
from arquivos import func_arquivos
from funcoes import valida_entrada_dados

if __name__ == "__main__":
    nome_opcao_desejada = menu.menu_principal()
    deletado = func_arquivos.deleta_registro_antigo(nome_opcao_desejada)
    if deletado:
        func_arquivos.gera_registro_novo(nome_opcao_desejada)

    opcao_escolhida = menu.menu_informacoes_concurso(nome_opcao_desejada)
    match opcao_escolhida:
        case "Conferir concursos":
            try:
                print(valida_entrada_dados.set_dezenas_concurso(
                    nome_opcao_desejada))

            except ValueError as vl:
                print(print(f"\033[31m{vl.args}\033[m"))
                print("\033[31mOpção informada inválida.\033[m")
                print("Obrigado por usar o sistema lotérica.")
            except IndexError as ie:
                print(print(f"\033[31m{ie.args}\033[m"))
                print("\033[31mOpção informada inválida.\033[m")
                print("Obrigado por usar o sistema lotérica.")
