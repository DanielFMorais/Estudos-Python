#Crie um programa que leia um número inteiro do usuário e diga se ele é par ou ímpar.

valor = int(input('Por favor, informe um número: '))

par_impar = valor % 2

if par_impar == 0:
    print (f'O número {valor} é um número PAR')
else: 
    print (f'O número {valor} é um número IMPAR')