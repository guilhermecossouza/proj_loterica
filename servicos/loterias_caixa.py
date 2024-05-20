from arquivos import grava_arquivos
import requests


def get_concursos():
    list_jogos_disponiveis = list()
    dict_jogos_disponiveis = dict()
    url = "https://loteriascaixa-api.herokuapp.com/api"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        for nome_jogos in resposta.json():
            if nome_jogos == "megasena":
                url = f"https://loteriascaixa-api.herokuapp.com/api/{nome_jogos}"
                resposta_concurso = requests.get(url=url)
                if resposta_concurso.status_code == 200:
                    dict_jogos_disponiveis["disponivel"] = nome_jogos
                    grava_arquivos.grava_arquivo_concurso_sorteado(
                        resposta_concurso.json())
                else:
                    dict_jogos_disponiveis["indisponivel"] = nome_jogos
                list_jogos_disponiveis.append(dict_jogos_disponiveis.copy())
                dict_jogos_disponiveis.clear()
        return list_jogos_disponiveis
    else:
        return None
