#Crie um programa que leia um número e informe se ele é positivo, negativo ou zero.

valor = input('Por favor, me informe um número: ')

int_valor = int(valor)


if int_valor < 0:
    print ('Isto é um valor negativo')
elif int_valor > 0:
    print ('Isto é um valor positivo')
elif int_valor == 0:
        print ('Isto é um zero')