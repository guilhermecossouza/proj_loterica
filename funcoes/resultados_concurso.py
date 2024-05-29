
import datetime
import os
import json


def conferindo_concurso(nome_concurso, numero_concurso, dezenas_jogadas=None):
    nome_arquivo = f"{datetime.datetime.today().strftime(
        "%Y-%m-%d")}-{nome_concurso}.json"
    caminho_arquivo = os.path.join("arquivos")
    caminho_completo = f"{caminho_arquivo}/{nome_arquivo}"
    if os.path.exists(caminho_completo):
        with open(caminho_completo, "r") as concurso:
            arquivo_concurso = json.load(concurso)

        if dezenas_jogadas:
            pass
        else:
            pass
    else:
        print("n existe")
