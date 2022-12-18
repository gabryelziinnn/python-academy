'''
Adie a função:  criar_funcao
Para que a mesma receba o argumento y, e então não dê erro de execução

'''
def soma(x, y):
    return x + y
    

def multiplica(x, y):
    return x * y

# recebo uma funcao e um parametro
def criar_funcao(func,x):
    # Aqui receberemos o ultimo parametro y, 
    def executa(y):
        return func(x,y)
    # E então retornaremos a função completa, no final
    return executa


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

# na chamada da função somente executaremos a mesma quando dermos o ultimo valor
print(soma_com_cinco(2))
print(multiplica_por_dez(4))