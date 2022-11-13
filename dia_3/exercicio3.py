'''

Exiba os indices da lista:

0 *nome*
1 *nome*
2 *nome*

'''

#Primeira forma

lista = ['Gabryel', 'Maria', 'João']
contador = 0

for nomes in lista:
    print(contador,nomes)
    contador = contador + 1

# Segunda forma
from itertools import count
lista = ['Gabryel', 'Maria', 'João']
indices = count(start=0, step=1)

while True:
    una = zip(indices , lista)
    print(list(una))
    break


# Forma correta
lista = ['Gabryel', 'Maria', 'João']

for valores, lista in enumerate(lista):
    print(valores, lista)