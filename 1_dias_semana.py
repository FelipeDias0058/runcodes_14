#Lê um número e exibe o dia correspondente
def f_d_semana(dia):
    if dia == 1:
        return "domingo"
    elif dia == 2:
        return "segunda-feira"
    elif dia == 3:
        return "terça-feira"
    elif dia == 4:
        return "quarta-feira"
    elif dia == 5:
        return "quinta-feira"
    elif dia == 6:
        return "sexta-feira"
    elif dia == 7:
        return "sábado"
    else:
        return "valor inválido"


def main():

    #Entrada de Dados
    dia = int(input(""))

    #Saída de Dados
    print(f_d_semana(dia))


if __name__ == '__main__':
    main()
