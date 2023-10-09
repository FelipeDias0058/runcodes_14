
#Calcula o valor a ser pago dos morangos
def v_morango(kg_morango):
    valor = 0
    if(kg_morango <= 5):
        valor = kg_morango * 2.5
    elif(kg_morango > 5):
        valor = kg_morango * 2.2

    return valor

#Calcula o valor a ser pago das maçãs
def v_maca(kg_maca):
    valor = 0 
    if(kg_maca <= 5):
        valor = kg_maca * 1.8
    elif(kg_maca > 5):
        valor = kg_maca * 1.5 
    return valor

#Calcula o valor do desconto
def f_desconto(valor):
    return valor - (valor*10/100)   

#Calcula o valor final a ser pago    
def valor_final(kg_maca, kg_morango):
    valor = v_maca(kg_maca) + v_morango(kg_morango)
    if((kg_maca + kg_morango) > 8 or ((v_maca(kg_maca) + v_morango(kg_morango)) > 25)):
        valor = f_desconto(valor)
    return valor


def main():

    #Entrada de Dados
    qtd_kg_morango = input()
    qtd_kg_maca = input()

    #Formata os dados como números reais
    qtd_kg_morango = float(qtd_kg_morango)
    qtd_kg_maca = float(qtd_kg_maca)

    #Executa a função 'valor_final'
    resultado = valor_final(qtd_kg_maca, qtd_kg_morango)

    #Saída de Dados
    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()
