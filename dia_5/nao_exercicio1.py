'''
Deve ser criado um sistema de perguntas e respostas dentro de dicionários na qual:
há um item correto
Exibe quando você acerta
Printa quantas perguntas voce acertou

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
'''

perguntas = {
    'Pergunta' : 'Qual meu sistema operacional preferido?',
    'Opções: ' : ['ubuntu', 'rancheros', 'debian', 'fedora'],
    
    'Pergunta' : 'Xaxa é bonita?',
    'Opções:' : ['demais', 'muito', 'cheira bem', 'excelente',]
}

print(perguntas['Pergunta'])

for x in perguntas.values():
    print(x)

#for a,b in pergunta.items():
#    print(a,b)


#print('\n'.join("{} : {}".format(k, v) for k, v in pergunta1.items()))