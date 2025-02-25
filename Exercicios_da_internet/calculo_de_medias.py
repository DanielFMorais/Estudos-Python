'''
numeros = [10, 20, 30, 40, 50]
Calcule a média dos valores dessa lista.

'''

numeros = [10, 20, 30, 40, 50]

soma = 0 

for numero in numeros: 
    soma += numero

media = soma / len(numeros)

print (f'A média dos valores é de: {media}')