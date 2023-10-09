
#As funções têm o propósito de validar a data DDMMAAA digitada
def f_dia_valido(data):
    dia = data[0] + data[1]
    
    return (31 >= int(dia) > 0)

def dia(data):
    dia = data[0] + data[1]
    if(31 >= int(dia) > 0):
        return int(dia)
    
def f_mes_valido(data):
    mes = data[2] + data[3]

    return (0 < int(mes) <= 12)

def mes(data):
    mes = data[2] + data[3]
    if(0 < int(mes) <= 12):
        return int(mes)

def f_ano_valido(data):
    ano = data[4] + data[5] + data[6] + data[7]

    return (10000 > int(ano) > 0)


#As funções usam o Bool para validar a data, levando em conta
#anos bissextos
def f_ano_bissexto(data):
    ano_dezena = data[6] + data[7]
    ano_centena = data[4] + data[5] + data[6] + data[7]
    status = False
    if(int(ano_dezena) % 4 == 0 and int(ano_dezena)!=0):
        status = True
    if(int(ano_centena)% 100 == 0 and int(ano_centena)% 400 == 0):
        status = True  
    if(int(data[4] + data[5] + data[6] + data[7]) == 1900):
        status = True    
    return status

def f_data_valida(data):
    if(f_ano_valido(data) and f_mes_valido(data) and f_dia_valido(data)):
        if((mes(data)==4 or mes(data)==6 or mes(data)== 9 or mes(data)==11) and dia(data) > 30):
            return False
        elif mes(data) == 2 and (dia(data) > 29 or (dia(data) > 28) and not f_ano_bissexto(data)):
            return False
        else:
            return True
    else:
        return False


def main():

    #Entrada de Dados (DDMMAAAA)
    data = input().strip()

    #Condicional chamando a função f_data_valida
    if(len(data) != 8):
        print('Falso')
    else:
        resultado = f_data_valida(data)

    #Saída de Dados ('True' ou 'False')    
    print(f'{resultado}')
    

if __name__ == '__main__':
    main()
    
