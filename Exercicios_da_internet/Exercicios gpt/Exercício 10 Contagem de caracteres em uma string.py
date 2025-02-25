'''
Crie um programa que leia uma palavra ou frase e conte quantos caracteres ela possui, desconsiderando os espaços.
'''

frase = input ('Por favor, digite algo: ')

contador = 0 
for caracteres in frase.replace(' ', ''):
    contador += 1 

print (f'A frase tem exatamente {contador} caracteres (sem contar espaços)')