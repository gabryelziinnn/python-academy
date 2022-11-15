'''
Crie uma função que fala se o número é par ou ímpar.

Retorne se o número é par ou impar.
'''

def impar_par(par_impar):
    numero = f'O número {par_impar} é par' if par_impar % 2 == 0 else f'O número {par_impar} é impar'
    print(numero)
    return par_impar

impar_par(3)