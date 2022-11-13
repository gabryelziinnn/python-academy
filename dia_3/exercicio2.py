"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Escreva seu primeiro nome, por favor: ')


while entrada.isalpha() == True:
    caracteres = len(entrada)
    if caracteres <= 4:
        print('Seu nome é curto')
        break
    elif caracteres > 4 and caracteres < 7:
        print('Seu nome é normal')
        break
    else:
        print('Seu nome é muito grande',caracteres)
        break
