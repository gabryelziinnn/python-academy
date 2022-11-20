'''
Crie 3 funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
'''

def multiplicacao():
    def dup(numero,multiplica):
        return numero * multiplica
    return dup

calc1 = multiplicacao()



print(calc1(20,2))
print(calc1(20,3))
print(calc1(20,4))



