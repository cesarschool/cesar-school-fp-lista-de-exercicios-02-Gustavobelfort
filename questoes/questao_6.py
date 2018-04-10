## QUESTÃO 6 ##
# Escreva um programa que calcule a porcentagem de nucleotídeos A, C, G e T em 
# uma cadeia de DNA informada pelo usuário. Indicar também a quantidade e a 
# porcentagem de nucleotídeos inválidos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():

    #recebe input do usuário e transforma em array
    cadeia = input('Digite a cadeia de DNA a ser analizada (A,T,G,C): ')
    cadeia = list(cadeia)

    #porcentagem de nucleotídeos no array
    porA = ( cadeia.count('A') / len(cadeia) ) * 100
    porT = ( cadeia.count('T') / len(cadeia) ) * 100
    porG = ( cadeia.count('G') / len(cadeia) ) * 100
    porC = ( cadeia.count('C') / len(cadeia) ) * 100

    #conta nucleotídeos inválidos
    invalidos = len(cadeia) - cadeia.count('A') - cadeia.count('C') - cadeia.count('G') - cadeia.count('T')
    porInvalidos = ( invalidos / len(cadeia) ) * 100

    print('O número de nucleotídeos inválidos é: {} o que equivale a {}% do total de nucleotídeos.'.format(invalidos, porInvalidos))
    print('A porcentagem de nucleotídeos A é de: {}%'.format(porA))
    print('A porcentagem de nucleotídeos T é de: {}%'.format(porT))
    print('A porcentagem de nucleotídeos G é de: {}%'.format(porG))
    print('A porcentagem de nucleotídeos C é de: {}%'.format(porC))
    
    #imprime a cadeia
    print(cadeia)


    
if __name__ == '__main__':
    main()
