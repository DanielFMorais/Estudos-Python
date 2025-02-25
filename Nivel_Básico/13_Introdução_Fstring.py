# fstr funciona para basicamente, colocar variáveis dentro de strings, e para isso vc colocar inicialmente um 
# f no inicio da string, e colocar em chaves {} o que vc quer que seja considerado a variável

"""
nome = 'Daniel Fernandes de Morais'
altura = 1.75
peso = 85
imc = peso / altura ** 2                                    #texto base

print (nome, 'tem exatamente', altura, 'de altura')
print (nome, ' tem também exatos', peso, 'KG')   
print ('devido a isto, seu IMC =', imc)
"""

nome = 'Daniel Fernandes de Morais'
altura = 1.75
peso = 85
imc = peso / altura ** 2

linha1 = f'{nome} tem {altura:.2f} de altura' # AQUI USAMOS O .2F QUE É BASICAMENTE DEFINIR  A QUANTIDADE DE CASAS DECIMAIS QUE IRÃO APARECER, SE VC COLOCAR UMA VIRGULA , ANTES 
# A PARTE INTEIRA SERA DIVIDIDA POR VIRGULAS QUANDO NECESSARIO EM CASO DE NUMEROS MUITO GRANDES, COMO USADO PARA MOEDAS
linha2 = f'{nome} tem também exatos {peso:.2f} kg'
linha3=  f'Devido a isto, seu IMC = {imc:.2f}' # o .2f só funciona caso for usado no f'

print (linha1)
print (linha2)   
print (linha3)

print (nome, 'tem exatamente', altura, 'de altura')