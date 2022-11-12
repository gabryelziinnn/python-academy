"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Digite um número inteiro: ')

if entrada.isdigit() == False:
    print('Você não digitou um número!')

while entrada.isdigit() == True:
    x = int(entrada)
    if x % 2 == 0:
        print('Seu número é par')
        break
    else:
        print('Seu numero é impar')
        break     
