'''
repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinido -> quando um código não tem fim ]

break -> serve para sair do laço do while, evitando assim que o programa fique em loop infinito, é uma forma de limitar o while
'''

condicao = True

while condicao:
    nome = input ('Qual o seu nome: ')
    print (f'O sue nome é {nome}')

    if nome == 'sair':
        break

print ('Acabou')