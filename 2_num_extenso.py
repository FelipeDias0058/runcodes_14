
#Identifica centenas, dezenas e unidades no número digitado
def f_extenso(numero):
    centena = ''
    dezena = ''
    unidade = ''
    
    if(len(numero) == 3):
       if(numero[0] == '1'):
           centena = 'uma centena'
       elif(numero[0] == '2'):
           centena = 'duas centenas'
       elif(numero[0] == '3'):
           centena = 'três centenas'
       elif(numero[0] == '4'):
           centena = 'quatro centenas'
       elif(numero[0] == '5'):
           centena = 'cinco centenas'
       elif(numero[0] == '6'):
           centena = 'seis centenas'
       elif(numero[0] == '7'):
           centena = 'sete centenas'
       elif(numero[0] == '8'):
           centena = 'oito centenas'
       elif(numero[0] == '9'):
           centena = 'nove centenas'
       if(numero[1] == '1'):
           dezena = 'uma dezena'
       elif(numero[1] == '2'):
           dezena = 'duas dezenas'
       elif(numero[1] == '3'):
           dezena = 'três dezenas'
       elif(numero[1] == '4'):
           dezena = 'quatro dezenas'
       elif(numero[1] == '5'):
           dezena = 'cinco dezenas'
       elif(numero[1] == '6'):
           dezena = 'seis dezenas'
       elif(numero[1] == '7'):
           dezena = 'sete dezenas'
       elif(numero[1] == '8'):
           dezena = 'oito dezenas'
       elif(numero[1] == '9'):
           dezena = 'nove dezenas'
       if(numero[2] == '1'):
           unidade = 'uma unidade'
       elif(numero[2] == '2'):
           unidade = 'duas unidades'
       elif(numero[2] == '3'):
           unidade = 'três unidades'
       elif(numero[2] == '4'):
           unidade = 'quatro unidades'
       elif(numero[2] == '5'):
           unidade = 'cinco unidades'
       elif(numero[2] == '6'):
           unidade = 'seis unidades'
       elif(numero[2] == '7'):
           unidade = 'sete unidades'
       elif(numero[2] == '8'):
           unidade = 'oito unidades'
       elif(numero[2] == '9'):
           unidade = 'nove unidades'    

    if(len(numero) == 2):
       if(numero[0] == '1'):
           dezena = 'uma dezena'
       elif(numero[0] == '2'):
           dezena = 'duas dezenas'
       elif(numero[0] == '3'):
           dezena = 'três dezenas'
       elif(numero[0] == '4'):
           dezena = 'quatro dezenas'
       elif(numero[0] == '5'):
           dezena = 'cinco dezenas'
       elif(numero[0] == '6'):
           dezena = 'seis dezenas'
       elif(numero[0] == '7'):
           dezena = 'sete dezenas'
       elif(numero[0] == '8'):
           dezena = 'oito dezenas'
       elif(numero[0] == '9'):
           dezena = 'nove dezenas'
       if(numero[1] == '1'):
           unidade = 'uma unidade'
       elif(numero[1] == '2'):
           unidade = 'duas unidades'
       elif(numero[1] == '3'):
           unidade = 'três unidades'
       elif(numero[1] == '4'):
           unidade = 'quatro unidades'
       elif(numero[1] == '5'):
           unidade = 'cinco unidades'
       elif(numero[1] == '6'):
           unidade = 'seis unidades'
       elif(numero[1] == '7'):
           unidade = 'sete unidades'
       elif(numero[1] == '8'):
           unidade = 'oito unidades'
       elif(numero[1] == '9'):
           unidade = 'nove unidades'    
    if(len(numero) == 1):
       if(numero[0] == '1'):
           unidade = 'uma unidade'
       elif(numero[0] == '2'):
           unidade = 'duas unidades'
       elif(numero[0] == '3'):
           unidade = 'três unidades'
       elif(numero[0] == '4'):
           unidade = 'quatro unidades'
       elif(numero[0] == '5'):
           unidade = 'cinco unidades'
       elif(numero[0] == '6'):
           unidade = 'seis unidades'
       elif(numero[0] == '7'):
           unidade = 'sete unidades'
       elif(numero[0] == '8'):
           unidade = 'oito unidades'
       elif(numero[0] == '9'):
           unidade = 'nove unidades'
    return centena, dezena,  unidade  

#Formata o texto que será exibido  
def f_num_extenso_format(numero):

    c, d, u = f_extenso(numero)
    if(len(numero)== 3 and numero[1]!= '0' and numero[2]!='0' and numero[0] != '0'):
        print(f'{c}, {d} e {u}.')
    if(len(numero)== 3 and numero[1]== '0' and numero[2]=='0' and numero[0] != '0'):
        print(f'{c}.')
    if(len(numero)== 3 and numero[1]== '0' and numero[2]!='0' and numero[0] != '0'):
        print(f'{c} e {u}.')
    if(len(numero)== 3 and numero[1]!= '0' and numero[2]=='0' and numero[0] != '0'):
        print(f'{c} e {d}.')
    if(len(numero)== 2 and numero[1]!= '0' and numero[0]!='0'):
        print(f'{d} e {u}.')
    if(len(numero)== 2 and numero[1]== '0' and numero[0]!='0'):
        print(f'{d}.')
    if(len(numero)== 2 and numero[1]!= '0' and numero[0]=='0'):
        print(f'{u}.')
    if(len(numero)== 1):
        print(f'{u}.')   

def main():
    #Entrada de Dados (número menor que 1000)
    numero = input().strip()

    #Saída de Dados
    f_num_extenso_format(numero)


if __name__ == '__main__':
    main()

    
