
from arquivos import func_arquivos


def ultimo_concurso(nome_concurso):
    dados_concurso = None
    arquivo_concurso = func_arquivos.busca_arquivo(nome_concurso)
    if arquivo_concurso:
        for concurso in arquivo_concurso:
            dados_concurso = concurso
            break
    return dados_concurso


def conferindo_concurso(nome_concurso, numero_concurso, dezenas_jogadas=None):
    informacoes = None
    arquivo_concurso = func_arquivos.busca_arquivo(nome_concurso)
    if arquivo_concurso:
        for concurso in arquivo_concurso:
            if int(numero_concurso) == concurso["concurso"]:
                informacoes = concurso
                break
            else:
                informacoes = None
    else:
        informacoes = None
    return informacoes


def conferi_dezenas(dezenas_jogadas, dezenas_sorteadas):
    dezenas_sorteadas = [int(numero) for numero in dezenas_sorteadas]
    dezenas_acerto = [
        numero for numero in dezenas_jogadas if dezenas_sorteadas.count(numero) > 0]
    return f"Você teve um total de {len(dezenas_acerto)} acertos, e as dezenas foram {dezenas_acerto}"


def dezenas_mais_sorteadas(nome_concurso):
    dezenas = list()
    arquivo_concurso = func_arquivos.busca_arquivo(nome_concurso)
    if arquivo_concurso:
        for concurso in arquivo_concurso:
            for dezena in concurso.get("dezenas"):
                dezenas.append(int(dezena))

        mais_sorteadas = None
        match nome_concurso:
            case "maismilionaria":
                dezena_incial_volante = 1
                dezena_final_volante = 50
                mais_sorteadas = trabalhando_dezenas(dezena_incial_volante,
                                                     dezena_final_volante, dezenas)
            case "megasena":
                dezena_incial_volante = 1
                dezena_final_volante = 60
                mais_sorteadas = trabalhando_dezenas(dezena_incial_volante,
                                                     dezena_final_volante, dezenas)
            case "lotofacil":
                dezena_incial_volante = 1
                dezena_final_volante = 25
                mais_sorteadas = trabalhando_dezenas(dezena_incial_volante,
                                                     dezena_final_volante, dezenas)
            case "quina":
                dezena_incial_volante = 1
                dezena_final_volante = 80
                mais_sorteadas = trabalhando_dezenas(dezena_incial_volante,
                                                     dezena_final_volante, dezenas)
            case "lotomania":
                dezena_incial_volante = 1
                dezena_final_volante = 100
                mais_sorteadas = trabalhando_dezenas(dezena_incial_volante,
                                                     dezena_final_volante, dezenas)
            case "timemania":
                dezena_incial_volante = 1
                dezena_final_volante = 80
                mais_sorteadas = trabalhando_dezenas(dezena_incial_volante,
                                                     dezena_final_volante, dezenas)
            case "duplasena":
                dezena_incial_volante = 1
                dezena_final_volante = 50
                mais_sorteadas = trabalhando_dezenas(dezena_incial_volante,
                                                     dezena_final_volante, dezenas)
            case "diadesorte":
                dezena_incial_volante = 1
                dezena_final_volante = 31
                mais_sorteadas = trabalhando_dezenas(dezena_incial_volante,
                                                     dezena_final_volante, dezenas)
            case "supersete":
                mais_sorteadas = trabalhando_dezenas_super_sete(
                    arquivo_concurso)
            case _:
                mais_sorteadas = None

    else:
        mais_sorteadas = None

    return mais_sorteadas


def trabalhando_dezenas_super_sete(dados_resultados):
    lista_dezenas = list()
    bloco = dict()
    lista_bloco_dezena = list()
    for numero in range(0, 7):
        lista_dezenas.clear()
        bloco.clear()
        for concurso in dados_resultados:
            lista_dezenas.append(int(concurso.get("dezenas")[numero]))

        for dezena in range(0, 10):
            bloco[str(dezena + 1)] = lista_dezenas.count(dezena)

        lista_bloco_dezena.append(
            dict(sorted(bloco.items(), key=lambda item: item[1], reverse=True)))

    return lista_bloco_dezena


def trabalhando_dezenas(inicio, termino, dezenas):
    dict_dezenas = dict()
    lista_dezenas = list()

    for dezena in range(inicio, termino + 1):
        dict_dezenas[str(dezena)] = dezenas.count(dezena)

    lista_dezenas.append(dict(
        sorted(dict_dezenas.items(), key=lambda item: item[1], reverse=True)))

    return lista_dezenas
