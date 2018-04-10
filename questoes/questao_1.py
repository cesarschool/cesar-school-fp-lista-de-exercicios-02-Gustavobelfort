## QUESTÃO 1 ##
# Faça um programa que receba cinco inteiros e diga qual deles é o maior e qual o menor.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    a = int(input('Digite o primeiro inteiro: '))
    b = int(input('Digite o segundo inteiro: '))
    c = int(input('Digite o terceiro inteiro: '))
    d = int(input('Digite o quarto inteiro: '))
    e = int(input('Digite o quinto inteiro: '))
    lista = [a, b, c, d ,e]
    lista.sort()
    print('O maior dos inteiros é: {}'.format(lista[-1]))
    print('O menor dos inteiros é: {}'.format(lista[0]))


if __name__ == '__main__':
    main()
    