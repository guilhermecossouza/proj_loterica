from menu import menu
from arquivos import func_arquivos
import regex


if __name__ == "__main__":
    nome_opcao_desejada = menu.menu_principal()
    deletado = func_arquivos.deleta_registro_antigo(nome_opcao_desejada)
    if deletado:
        func_arquivos.gera_registro_novo(nome_opcao_desejada)

    opcao_escolhida = menu.menu_informacoes_concurso(nome_opcao_desejada)
    match opcao_escolhida:
        case "Conferir concursos":
            try:
                numero_concurso = int(input("Informe o número do conceurso: "))
                conferir_dezenas = str(
                    input("Deseja conferir também as dezenas [S/N]? ")).strip().upper()[0]
                if conferir_dezenas == "S":
                    dezenas_jogo_realizado = str(
                        input("Informe as dezenas separadas por [,]: "))
                    dezenas = regex.compile(",")
                    if dezenas.search(dezenas_jogo_realizado):
                        dezenas_jogo_realizado = dezenas_jogo_realizado.replace(
                            " ", "")
                        func_arquivos.consuta_concurso_pelo_numero(
                            nome_opcao_desejada, dezenas_jogo_realizado)
                    else:
                        func_arquivos.consuta_concurso_pelo_numero(
                            numero_concurso)

            except ValueError as vl:
                print(print(f"\033[31m{vl.args}\033[m"))
                print("\033[31mOpção informada inválida.\033[m")
                print("Obrigado por usar o sistema lotérica.")
            except IndexError as ie:
                print(print(f"\033[31m{ie.args}\033[m"))
                print("\033[31mOpção informada inválida.\033[m")
                print("Obrigado por usar o sistema lotérica.")
