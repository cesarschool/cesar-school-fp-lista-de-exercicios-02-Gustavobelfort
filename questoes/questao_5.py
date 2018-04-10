## QUESTÃO 5 ##
# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é 
# Equilátero, Isósceles ou Escaleno.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    a = float(input('Digite a medida do primeiro lado:'))
    b = float(input('Digite a medida do segundo lado:'))
    c = float(input('Digite a medida do terceiro lado:'))

    isosceles = [a,b,c]

    if a == b and a == c :
        print('O triangulo é equilátero.')

    elif a != b and a != c :
        print('O triângulo é escaleno.')
    
    elif ( isosceles.count(a) or isosceles.count(b) or isosceles.count(c) ) == 2:
        print('O triângulo é isósceles.')



    
if __name__ == '__main__':
    main()
