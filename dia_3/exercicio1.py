"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
import time
HORARIO = time.strftime('%M')
entrada = input('Insira um horário: ')

while entrada.isdigit() == True:
    x = int(entrada)
    if x in range(0,12):
        print(f'Bom dia! são {entrada}:{HORARIO}')
        break
    elif x in range(12,18):
        print(f'Boa tarde! são {entrada}:{HORARIO}')
        break
    else:
        print(f'Boa noite! são {entrada}:{HORARIO}')
        break