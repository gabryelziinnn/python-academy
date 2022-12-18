import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# 1 Questao:
novos_produtos = copy.deepcopy(produtos)

novos_valores = [
    { **itens, 'preco' : round(itens['preco'] * 1.1, 2) }
    # com este for, pego todos os valores da lista
    for itens in novos_produtos
]
produtos = [nomes['nome'] for nomes in novos_valores]
valores = [valor['preco'] for valor in novos_valores]


# 2 questao:
lista_ordenada = copy.deepcopy(novos_valores)

lista_ordenada.sort(key=lambda itens:itens['nome'])
produtos_ordenados_por_nome = sorted(lista_ordenada, key=lambda itens:itens['nome'])


# 3 Questao:
ordenar = copy.deepcopy(produtos_ordenados_por_nome)

