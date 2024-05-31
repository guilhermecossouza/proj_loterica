from menu import menu
from arquivos import func_arquivos
from funcoes import resultados_concurso, valida_entrada_dados


if __name__ == "__main__":
    nome_opcao_desejada = menu.menu_principal()
    deletado = func_arquivos.deleta_registro_antigo(nome_opcao_desejada)
    if deletado:
        func_arquivos.gera_registro_novo(nome_opcao_desejada)

    opcao_escolhida = menu.menu_informacoes_concurso(nome_opcao_desejada)
    match opcao_escolhida:
        case "Último concurso":
            concurso = resultados_concurso.ultimo_concurso(nome_opcao_desejada)
            if concurso:
                print(f"\nInformações sobre {nome_opcao_desejada}")
                print(f"Concurso: {concurso.get("concurso")}")
                print(f"Realizado na data de: {concurso.get("data")}")
                print(f"Dezenas sorteadas foram: {concurso.get("dezenas")}\n")
            else:
                print("\033[31mNão foi possível mostrar as informações.\033[m")

        case "Consulta concurso":
            numero_concurso = valida_entrada_dados.numero_concurso(
                nome_opcao_desejada)

            concurso = resultados_concurso.conferindo_concurso(
                nome_opcao_desejada, numero_concurso)

            print(f"\nInformações sobre {nome_opcao_desejada}")
            print(f"Concurso: {concurso.get("concurso")}")
            print(f"Realizado na data de: {concurso.get("data")}")
            print(f"Dezenas sorteadas foram: {concurso.get("dezenas")}\n")

        case "Conferir dezenas":
            numero_concurso = valida_entrada_dados.numero_concurso(
                nome_opcao_desejada)

            desenas_jogada = valida_entrada_dados.set_dezenas_concurso(
                nome_opcao_desejada)

            concurso = resultados_concurso.conferindo_concurso(
                nome_opcao_desejada, numero_concurso, desenas_jogada)

            if concurso:
                print(f"\nInformações sobre {nome_opcao_desejada}")
                print(f"Concurso: {concurso.get("concurso")}")
                print(f"Realizado na data de: {concurso.get("data")}")
                print(f"Dezenas sorteadas foram: {concurso.get("dezenas")}")
                resposta = resultados_concurso.conferi_dezenas(
                    desenas_jogada, concurso.get("dezenas"))
                print(f"{resposta}\n")

            else:
                print("\033[31mNão foi possível mostrar as informações.\033[m")

        case "Dezenas mais sorteadas":
            resultados_concurso.dezenas_mais_sorteadas(nome_opcao_desejada)
