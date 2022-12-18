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
import dados_packages


# 1° Questão:

# valores formatados
for x in dados_packages.valores:
    novos = format(x, '.2f')
   # print(novos)

prod = ["{0}".format(i) for i in dados_packages.produtos]
val = ["{0:0.2f}".format(i) for i in dados_packages.valores]

print(f'{prod + val}')


# 2° Questão:
for valores in dados_packages.produtos_ordenados_por_nome:
    print(f'\b{valores}')


# 3° Questão:
dados_packages.ordenar.sort(key=lambda itens:itens['preco'])
produtos_ordenados_por_preco = sorted(dados_packages.ordenar, key=lambda itens:itens['preco'])

print()
print()

for preco in produtos_ordenados_por_preco:
    print(f'\b{preco}')