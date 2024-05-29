
import re


def numero_concurso(nome_concurso):
    while True:
        try:
            concurso = int(
                input(f"Informe o número do concurso {nome_concurso}: "))
            if concurso > 0:
                break
            else:
                print("\033[31mNúmero concurso inválido.\033[m")
        except ValueError as e:
            print("\033[31mInforme o número do concurso.\033[m")
            print(f"\033[31m{e.args}\033[m")
    return concurso


def conferir_dezenas():
    while True:
        try:
            resposta = str(
                input("Deseja conferir as dezenas também? [S/N]: ")).strip().upper()[0]
            if resposta == "S":
                conferir = True
                break
            elif resposta == "N":
                conferir = False
                break
            else:
                print("\033[31mOpção inválida! Informe S ou N.\033[m")
        except IndexError as e:
            print("\033[31mInforme S ou N.\033[m")
            print(f"\033[31m{e.args}\033[m")
    return conferir


def set_dezenas_concurso(nome_concurso):
    print(f"Concurso: {nome_concurso}")
    match nome_concurso:
        case "maismilionaria":
            qtd_dezenas_jogadas = 8
        case "megasena":
            qtd_dezenas_jogadas = 6
        case "lotofacil":
            qtd_dezenas_jogadas = 15
        case "quina":
            qtd_dezenas_jogadas = 4
        case "lotomania":
            qtd_dezenas_jogadas = 20
        case "timemania":
            qtd_dezenas_jogadas = 6
        case "duplasena":
            qtd_dezenas_jogadas = 11
        case "federal":
            qtd_dezenas_jogadas = 5
        case "diadesorte":
            qtd_dezenas_jogadas = 7
        case "supersete":
            qtd_dezenas_jogadas = 7

    while True:
        if nome_concurso == "federal":
            dezenas_jogadas = str(input(
                f"Informe as {qtd_dezenas_jogadas} jogos jogados, separadas por virgula [,]: ")).replace(" ", "")
        else:
            dezenas_jogadas = str(input(
                f"Informe as {qtd_dezenas_jogadas} dezenas jogadas, separadas por virgula [,]: ")).replace(" ", "")

        if dezenas_jogadas != "":
            lista_dezenas = get_valida_dezenas(nome_concurso, dezenas_jogadas)
            if lista_dezenas:
                break
            else:
                print(
                    f"\033[31mInforme as {qtd_dezenas_jogadas} dezenas separadas por [,].\033[m")
        else:
            print(
                f"\033[31mInforme as {qtd_dezenas_jogadas} dezenas separadas por [,].\033[m")
    return lista_dezenas


def get_valida_dezenas(nome_concurso, dezenas_informadas):
    match nome_concurso:
        case "maismilionaria":
            regex = re.compile(r"^[0-9]{2}+,[0-9,]{20}")
        case "megasena":
            regex = re.compile(r"^[0-9]{2}+,[0-9,]{14}")
        case "lotofacil":
            regex = re.compile(r"^[0-9]{2}+,[0-9,]{41}")
        case "quina":
            regex = re.compile(r"^[0-9]{2}+,[0-9,]{11}")
        case "lotomania":
            regex = re.compile(r"^[0-9]{2}+,[0-9,]{56}")
        case "timemania":
            regex = re.compile(r"^[0-9]{2}+,[0-9,]{17}")
        case "duplasena":
            regex = re.compile(r"^[0-9]{2}+,[0-9,]{32}")
        case "federal":
            regex = re.compile(r"^[0-9]{6}+,[0-9,]{27}")
        case "diadesorte":
            regex = re.compile(r"^[0-9]{2}+,[0-9,]{17}")
        case "supersete":
            regex = re.compile(r"^[0-9]{1}+,[0-9,]{11}")

    dezenas_validadas = regex.findall(dezenas_informadas)
    if dezenas_validadas:
        dezenas = dezenas_validadas[0]
        lista_dezenas = [int(numero)
                         for numero in dezenas.split(",")]
    else:
        lista_dezenas = []

    return lista_dezenas
