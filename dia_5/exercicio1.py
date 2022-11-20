'''
Deve ser criado um sistema de perguntas e respostas dentro de dicionários na qual:
há um item correto
Exibe quando você acerta
Printa quantas perguntas voce acertou
'''
'''
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
    'Qual meu sistema operacional preferido?'
    '\n\nOpções: ' : [
        { 1 : 'ubuntu'},
        { 2 : 'rancheros'},
        { 3 :'debian'},
        { 4 : 'fedora'},
    ],
    'Xaxa é bonita?'
    '\n\nOpções: ' : [
        { 1 : 'demais'},
        { 2 : 'muito'},
        { 3 : 'cheira bem'},
        { 4: 'excelente'},
    ],
}




for x, y in enumerate(perguntas.keys(),start=1):
    print(f'{x}) {y}')
    #for key in perguntas:
    #    print(perguntas[key])