'''

Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.

'''

def multiplica_func(*args):
    total = 1
    for num in args:
        total *= num
    print(total)
    return total

multiplica_func(2,6)