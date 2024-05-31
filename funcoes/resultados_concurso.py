
import datetime
import os
import json


def conferindo_concurso(nome_concurso, numero_concurso, dezenas_jogadas=None):
    informacoes = None
    nome_arquivo = f"{datetime.datetime.today().strftime(
        "%Y-%m-%d")}-{nome_concurso}.json"
    caminho_arquivo = os.path.join("arquivos")
    caminho_completo = f"{caminho_arquivo}/{nome_arquivo}"
    if os.path.exists(caminho_completo):
        with open(caminho_completo, "r") as concurso:
            arquivo_concurso = json.load(concurso)

        for concurso in arquivo_concurso:
            if int(numero_concurso) == concurso["concurso"]:
                informacoes = concurso
    else:
        print(f"\033[31mDados sobre {nome_concurso} não encontrados.\033[m")

    return informacoes


def ultimo_concurso(nome_concurso):
    nome_arquivo = f"{datetime.datetime.today().strftime(
        "%Y-%m-%d")}-{nome_concurso}.json"
    caminho_arquivo = os.path.join("arquivos")
    caminho_completo = f"{caminho_arquivo}/{nome_arquivo}"
    if os.path.exists(caminho_completo):
        with open(caminho_completo, "r") as concurso:
            arquivo_concurso = json.load(concurso)

        dados_concurso = None
        for concurso in arquivo_concurso:
            dados_concurso = concurso
            break

        return dados_concurso


def conferi_dezenas(dezenas_jogadas, dezenas_sorteadas):
    dezenas_sorteadas = [int(numero) for numero in dezenas_sorteadas]
    dezenas_acerto = [
        numero for numero in dezenas_jogadas if dezenas_sorteadas.count(numero) > 0]
    return f"Você teve um total de {len(dezenas_acerto)} acertos, e as dezenas foram {dezenas_acerto}"
