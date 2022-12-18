'''
copy, sorted, produtos.sort
Exercícios
Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)

Segue a lista abaixo:
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

Ordene os produtos por nome decrescente (do maior para menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

Ordene os produtos por preco crescente (do menor para maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
'''
import dados_packages, copy


# 1° Questão:

novos_produtos = copy.deepcopy(dados_packages.produtos)
novos_valores = [
    { **itens, 'preco' : round(itens['preco'] * 1.1, 2) }
    # com este for, pego todos os valores da lista
    for itens in novos_produtos
]
produtos = [nomes['nome'] for nomes in novos_valores]
valores = [valor['preco'] for valor in novos_valores]

# valores formatados
for x in valores:
    novos = format(x, '.2f')
   # print(novos)

prod = ["{0}".format(i) for i in produtos]
val = ["{0:0.2f}".format(i) for i in valores]

print(f'{prod + val}')


# 2° Questão:
lista_ordenada = copy.deepcopy(novos_valores)
lista_ordenada.sort(key=lambda itens:itens['nome'])

produtos_ordenados_por_nome = sorted(lista_ordenada, key=lambda itens:itens['nome'])

for valores in produtos_ordenados_por_nome:
    print(f'\b{valores}')


# 3° Questão:
ordenar = copy.deepcopy(produtos_ordenados_por_nome)
ordenar.sort(key=lambda itens:itens['preco'])

produtos_ordenados_por_preco = sorted(ordenar, key=lambda itens:itens['preco'])

print()
print()

for preco in produtos_ordenados_por_preco:
    print(f'\b{preco}')