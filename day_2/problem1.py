'''
Retorna o número (contagem) de vogais na string fornecida.

Consideraremos a, e, i, o, u como vogais.

A string de entrada consistirá apenas em letras minúsculas e/ou espaços.
'''
import re

vogais = input('Insira somente vogais no texto: ')


while True:
   if not re.findall('[aeiou]', vogais):    
       print(f'Você deve inserir somente vogais e suas palavraas: {vogais}')
       break
   else:
        print(f'Voce digitou corretamente:{vogais.lower()}')
        break

