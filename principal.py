from menu import menu
from arquivos import grava_arquivos


if __name__ == "__main__":
    nome_opcao_desejada = menu.menu_principal()
    deletado = grava_arquivos.deleta_registro_antigo(nome_opcao_desejada)
    if deletado:
        grava_arquivos.gera_registro_novo(nome_opcao_desejada)
    else:
        pass
