
import re


def set_dezenas_concurso(nome_concurso):
    match nome_concurso:
        case "maismilionaria":
            print(f"Concurso: {nome_concurso}")
            while True:
                dezenas_jogadas = str(input(
                    "Informe as oito dezenas jogadas, separadas por virgula [,]: ")).replace(" ", "")
                if dezenas_jogadas != "":
                    regex = re.compile(r"^[1-9]{2}+,[1-9,]{20}")
                    dezenas_validadas = regex.findall(dezenas_jogadas)
                    if dezenas_validadas:
                        dezenas = dezenas_validadas[0]
                        lista_dezenas = [int(numero)
                                         for numero in dezenas.split(",")]
                        break
                    else:
                        print(
                            "\033[31mInforme as oito dezenas separadas por [,].\033[m")
                else:
                    print("\033[31mInforme as dezenas.\033[m")
            return lista_dezenas
