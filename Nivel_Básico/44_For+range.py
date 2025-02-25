"""
For + Range ELAS NÃO DEPENDEM UMA DA OUTRA

range -> range (start, stop, step) AQUI DETERMINA O INICIO DO RANGE, DEPOIS O FINAL E DEPOIS DE QUANTO EM QUANTOS PULAR, ele sozinho sem valores complementares representa o final
"""

numeros = range(5, 10, 2) # isso pode ser tanto positivo quanto negativo  

for numero in numeros:
    print (numero)