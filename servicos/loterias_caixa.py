from arquivos import grava_arquivos
import requests


def get_nome_jogos_oferecidos():
    url = "https://loteriascaixa-api.herokuapp.com/api"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None


def get_concursos_sorteados(nome_concurso):
    url = f"https://loteriascaixa-api.herokuapp.com/api/{nome_concurso}/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        concursos = resposta.json()
    else:
        concursos = None
    return concursos
