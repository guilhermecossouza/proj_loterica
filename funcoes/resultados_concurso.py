
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

        match nome_concurso:
            case "maismilionaria":
                dezena_incial_volante = 1
                dezena_final_volante = 50
            case "megasena":
                dezena_incial_volante = 1
                dezena_final_volante = 60
            case "lotofacil":
                dezena_incial_volante = 1
                dezena_final_volante = 25
            case "quina":
                dezena_incial_volante = 1
                dezena_final_volante = 80
            case "lotomania":
                dezena_incial_volante = 1
                dezena_final_volante = 100
            case "timemania":
                dezena_incial_volante = 1
                dezena_final_volante = 80
            case "duplasena":
                dezena_incial_volante = 1
                dezena_final_volante = 50
            case "federal":
                dezena_incial_volante = 1
                dezena_final_volante = 5
            case "diadesorte":
                dezena_incial_volante = 1
                dezena_final_volante = 31
            case "supersete":
                dezena_incial_volante = 0
                dezena_final_volante = 9
                
        

    else:
        dezenas_mais_sorteadas = None

    print(dezenas)
