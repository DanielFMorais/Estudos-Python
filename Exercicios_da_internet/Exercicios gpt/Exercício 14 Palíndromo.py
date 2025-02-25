'''
Crie um programa que peça ao usuário uma palavra e verifique se ela é um palíndromo. 
Uma palavra é um palíndromo se puder ser lida da mesma forma de trás para frente (ex.: "arara", "radar").
'''


palavra = input ('Por favor, me informe a palavra: ').lower()

palavra_invertida = palavra[::-1]

if palavra_invertida == palavra:
    print (f'A palavra informada é um palíndromo')
else:
    print (f'A palavra informada NÃO é um palíndromo')