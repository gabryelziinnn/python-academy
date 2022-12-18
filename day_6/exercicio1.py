'''
Você recebe uma sequência de letras e uma matriz de números. 
Os números indicam as posições das letras que devem ser retiradas, em ordem, começando do início do array. 
Após cada remoção, o tamanho da corda diminui (não há espaço vazio). 
Devolva a única letra restante. 

Exemplo: 

let str = "zbk", arr = [0, 1]
    str = "bk", arr = [1]
    str = "b", arr = []
    return 'b'


Notas A string fornecida nunca estará vazia. 
O comprimento da matriz é sempre um a menos que o comprimento da string. 
Todos os números são válidos. 
Pode haver letras e números duplicados.

'''

def last_survivor(letters, coords): 
    strings = letters
    deletar = coords
    lista = []
    for palavras in strings:
        lista.append(palavras)
    for delecoes in sorted(deletar, reverse=True):
        del lista[delecoes]
    nova_palavra = ''.join(map(str,lista))
    print(nova_palavra)
    return nova_palavra
last_survivor('zbk',[0,1])
