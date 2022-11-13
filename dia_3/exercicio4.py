"""

Faça uma lista de compra com listas.
o usuário deve ter a possibilidade de inserir, apagar e listar os valores da sua lista.
Não permita que o programa quebre com quaisquer erros.

"""

lista = []

try:
    while True:
        entrada = input('Selecione as opções: [i]nserir, [a]pagar, [l]istar: ')
        if entrada == 'i':
            insira = input('Insira seu produto: ')
            if insira.isalpha():
                lista.append(insira)
            else:
                print('Insira somente palavras!')
        elif entrada == 'l':
            nova = lista.copy()
            for x, nova in enumerate(nova):
                print(x, nova)
        elif entrada == 'a':
            apagar = int(input('Insira o index a ser apagado: '))
            lista.pop(apagar)
        else:
            print("Por favor, escolha as opções: [i], [a] ou [l]!")
except IndexError as index_erro:
    print(f'Esse index {index_erro} está fora do range!')
except ValueError as valor:
    print(f'Insira somente números para apagar os elementos!', valor)
except Exception as desconhecido:
    print(f'Ocorreu algum erro desconhecido: {desconhecido}')