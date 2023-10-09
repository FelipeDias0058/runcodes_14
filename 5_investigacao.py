
#A função conta quantas respostas afirmativas
def f_sim_count(r):
    score = 0
    r = str(r).lower()
    if(r == 's'):
        score += 1
    elif (r == 'n'):
        score += 0
    else:
        raise ValueError(f'Digite "s" ou "n"')
    return score

#Dependendo das respostas, faz determinada acusação
def f_acusacao(score):
    status = ''
    if(score < 2):
        status = 'Inocente'
    elif(score == 2):
        status = 'Suspeito'
    elif(score == 3 or score == 4):
        status = 'Cúmplice'
    elif(score == 5):
        status = 'Assassino' 

    return status         


def main():

    #Entrada de Dados
    print("Responda as perguntas com 's' ou 'n'.\n")
    print("Telefonou para a vítima ?")
    score = 0
    r = input().strip()
    score += f_sim_count(r)

    print("Esteve no local do crime ?")
    r = input().strip()
    score += f_sim_count(r)

    print("Mora perto da vítima ?")
    r = input().strip()
    score += f_sim_count(r)

    print("Devia para a vítima ?")
    r = input().strip()
    score += f_sim_count(r)

    print("Já trabalhou com a vítima ?")
    r = input().strip()
    score += f_sim_count(r)


    #Chama a função 'f_acusacao'
    acusacao = f_acusacao(score)

    #Saída de Dados
    print(f'{acusacao}')


if __name__ == '__main__':
    main()
