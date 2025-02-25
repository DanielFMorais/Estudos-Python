# exercicio - sistema de pergutnas e respostas 


pergunta = [
    dict(
        pergunta = 'Quanto é 10 + 10',
        opcoes = ['10', '15', '29', '20'], 
        resposta = '20',
    ),
    dict(
        pergunta = 'Qual o ano em que estamos?',
        opcoes = ['2024', '2025', '1987', '2026'],
        resposta = '2025',
    ),
    dict(
        pergunta = 'Qual a captal do Brasil?',
        opcoes = ['Brasilia', 'Belo horizonte', 'São paulo', 'Rio de janeiro'],
        resposta = 'Brasilia',
    ),
]

contador_acerto = {'valor' : 0}

def sistema_perguntas (dicionario, perguntas, opcoes):
    print('==' * 30)
    print (f"Pergunta: {pergunta[dicionario][perguntas]}")
    print()
    print ('Opções:')
    print()
    
    for indice, opcoest  in enumerate(pergunta[dicionario][opcoes]):
        print(indice, opcoest) 
    
    qtd_opcoes = len(pergunta[dicionario][opcoes])
    resposta_indice = (input ('Qual a resposta certa?: '))

    if resposta_indice.isdigit() and int(resposta_indice) < qtd_opcoes:
        resposta_indice_int = int(resposta_indice)
        resposta_tex = pergunta[dicionario][opcoes][resposta_indice_int]
        print ()

        if resposta_tex == pergunta[dicionario]['resposta']:
            print ('Você acertou!')
            contador_acerto ['valor'] += 1
        else:
            print ('Você errou')
    else:
        print ('Por favor, informe um valor válido')
        


sistema_perguntas(0,'pergunta', 'opcoes')
sistema_perguntas(1,'pergunta', 'opcoes')
sistema_perguntas(2,'pergunta', 'opcoes')

print('==' * 30)
print (f'Você acertou exatamente: {contador_acerto['valor']} questões')
print('==' * 30)

