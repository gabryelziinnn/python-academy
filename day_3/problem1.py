"""
Escreva uma função que aceite um inteiro n e uma string s como parâmetros,
e retorna uma string de s repetida exatamente n vezes.

Exemplo (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
"""

def repeat_str(repeat, string):
    repeat = int(repeat)
    soma = repeat * string
    print(soma)
    return soma

repeat_str(str(4),'a')
repeat_str(str(3),'hello')
repeat_str(str(2),'abc')

