import datetime
import os
import json
from pathlib import Path
from servicos import loterias_caixa


def deleta_registro_antigo(nome_concurso):
    nome_arquivo = f"{datetime.datetime.today().strftime(
        "%Y-%m-%d")}-{nome_concurso}.json"
    caminho_completo = f"{os.path.join("arquivos")}/{nome_arquivo}"
    deletado = False
    if not os.path.exists(caminho_completo):
        caminho_pasta = Path("arquivos")
        for nome_arquivo in caminho_pasta.rglob("*.json"):
            if nome_concurso in nome_arquivo.name:
                os.remove(nome_arquivo)
        deletado = True
    return deletado


def gera_registro_novo(nome_concurso):
    concursos = loterias_caixa.get_concursos_sorteados(nome_concurso)
    nome_arquivo = f"{datetime.datetime.today().strftime(
        "%Y-%m-%d")}-{nome_concurso}.json"
    caminho_arquivo = os.path.join(f"arquivos/{nome_arquivo}")
    if concursos:
        with open(caminho_arquivo, "w") as arquivo:
            json.dump(concursos, arquivo, indent=4)


def busca_arquivo(nome_concurso):
    nome_arquivo = f"{datetime.datetime.today().strftime(
        "%Y-%m-%d")}-{nome_concurso}.json"
    caminho_arquivo = os.path.join("arquivos")
    caminho_completo = f"{caminho_arquivo}/{nome_arquivo}"
    arquivo_concurso = None
    if os.path.exists(caminho_completo):
        with open(caminho_completo, "r") as concurso:
            arquivo_concurso = json.load(concurso)
    else:
        print(f"\033[31mDados sobre {nome_concurso} não encontrados.\033[m")

    return arquivo_concurso
