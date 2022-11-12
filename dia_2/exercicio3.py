carrinho = []

carrinho.append(('Prod1', 30.30))
carrinho.append(('Prod2', 10.40))
carrinho.append(('Prod3', 40))
carrinho.append(('Prod4', 50))
carrinho.append(('Prod5', 60))


"""pego o index dos valores, e somo os mesmos"""
multi = sum([valor[1] for valor in carrinho])

print(multi)