'''
palavras = ["python", "asimov", "código", "web", "programação"]

Crie um código que seja capaz de encontrar e exibir a maior e a menor palavra da lista (em número de caracteres).

'''
palavras = ["python", "asimov", "código", "web", "programação"]


maior_palavra = palavras [0]
menor_palavra = palavras [0]

for palavra in palavras:
    if len(palavra) > len (maior_palavra):
        maior_palavra = palavra
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print (f'A menor palavra é: {menor_palavra}')
print (f'A maior palavra é: {maior_palavra}')
