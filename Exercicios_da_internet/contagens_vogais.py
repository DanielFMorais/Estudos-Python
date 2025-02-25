'''
Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) há na frase.
'''

palavra = input ('Por favor, me informe a palavra: ')

def quantidade (palavra):
    vogais = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U' ]
    
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

print (f'A palavra "{palavra}" tem exatamente: {quantidade(palavra)} vogais')
