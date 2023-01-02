'''

Exercício - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista.

Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

'''

lista_a = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_b = ['BA', 'SP', 'MG', 'RJ']

def merger(lista1,lista2):
    answer = []
    def solucao(lista1,lista2):
        for indices in range(len(lista1)):
            a=lista1[indices]
            b=lista2[indices]
            temp = [a,b]
            answer.append(temp)
        return solucao
    if len(lista1) < len(lista2):
        lista1.append('None')
        solucao(lista1,lista2)
    elif len(lista2) < len(lista1):
        lista2.append('None')
        solucao(lista1,lista2)
    else:        
        solucao(lista1,lista2)
    return answer
x = merger(lista_a,lista_b)
print(x)



# Solução correta
from itertools import zip_longest
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']

estados = ['BA', 'SP', 'MG', 'RJ']


cidades_estados = zip_longest(cidades,estados, fillvalue='Não há um valor correspondente')

for cidades, estados in cidades_estados:
    print(f'A Cidade é: {cidades}, e seu respectivo Estado: {estados}')
