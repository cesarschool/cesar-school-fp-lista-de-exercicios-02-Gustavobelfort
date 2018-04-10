# %load questao_8.py
## QUESTÃO 8 ##
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

def bissexto(ano):
    if ( ano % 4 ) == 0 :
        return True
    elif ( ano % 100 ) == 0 and ( ano % 400 ) == 0 :
        return True
    else :
        return False

def main():
    data = input('Data:')
    ano,mes,dia = data.split('-')
    
    
    if bissexto(int(ano)) == True :
        if dia == "29" and mes == "02" :
            dia = "01"
            mes = int(mes) + 1
            
    elif dia == "28" and mes == "02" :
        dia = "01"
        mes = int(mes) + 1
    
    
    if (int(mes) == 1 or int(mes) == 3 or int(mes) == 5 or int(mes) == 7 or int(mes) == 8 or int(mes) == 10 or int(mes) == 12) and dia == "31" :
        dia = "01"
        mes = int(mes) + 1
    
    if (int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11) and dia == "30" :
        dia = "01"
        mes = int(mes) + 1
    
    if (not (dia == "31") and not (dia == "30")) and ((not dia == "28" or not dia == "29") and (mes == "02")) :
        dia = int(dia) + 1
    
    if int(mes) > 12 :
        ano = int(ano) + 1
        mes = 1
        dia = 1
        
    print(ano,"-",mes,"-",dia)
    
if __name__ == '__main__':
    main()
