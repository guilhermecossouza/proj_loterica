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
        case "Conferir concursos":
            numero_concurso = valida_entrada_dados.numero_concurso(
                nome_opcao_desejada)
            conferir = valida_entrada_dados.conferir_dezenas()
            if conferir:
                dezenas_jogadas = valida_entrada_dados.set_dezenas_concurso(
                    nome_opcao_desejada)
                resultados_concurso.conferindo_concurso(
                    nome_opcao_desejada, numero_concurso, dezenas_jogadas)
            else:
                resultados_concurso.conferindo_concurso(
                    nome_opcao_desejada, numero_concurso)
