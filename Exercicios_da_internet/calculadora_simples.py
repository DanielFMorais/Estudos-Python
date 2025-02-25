'''
Crie uma calculadora simples que leia dois números e escolha entre as operações de soma, subtração, multiplicação e divisão.
'''

import sys 

def transformacao_int (valor):
    if valor.isdigit():
        return (valor)
    else:
        print ('Por favor, digite um valor em números.')
        sys.exit()

primeiro_valor = input ('Qual o primeiro valor: ')
primeiro_valor = transformacao_int (primeiro_valor)

segundo_valor = input ('Qual o segundo valor: ')
segundo_valor = transformacao_int (segundo_valor) 

operacao = input ('Qual operação deseja realizar [1] soma; [2] subtração; [3] multiplição; [4] divisão: ')



if operacao == '1':
    print (f'{primeiro_valor}+{segundo_valor} = {primeiro_valor+segundo_valor}')
elif operacao == '2':
    print (f'{primeiro_valor}-{segundo_valor} = {primeiro_valor-segundo_valor}')
elif operacao == '3':
    print (f'{primeiro_valor}x{segundo_valor} = {primeiro_valor*segundo_valor}')
elif operacao == '4':
    if segundo_valor != 0:
        print (f'{primeiro_valor}/{segundo_valor} = {primeiro_valor/segundo_valor}')
    else: 
        print ('Não se pode dividir por zero')
else: 
    print ('Escolha uma das opções de digitando de 1 à 4')
        