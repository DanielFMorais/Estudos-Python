'''

Seu objetivo é encontrar o segundo maior valor da lista (supondo que ela possua pelo menos dois elementos).
'''

numeros = [32, 10, 58, 30, 55, 12, 28, 51]

numeros.sort() #ordena as coisas de forma crescente
segundo_maior = numeros [-2]

print('O segundo maior valor é: ', segundo_maior)

