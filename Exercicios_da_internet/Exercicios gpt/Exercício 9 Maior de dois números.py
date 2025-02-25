#Crie um programa que leia dois números e mostre o maior deles.

valor1 = float(input ('Por favor, me informe o primeiro valor: '))
valor2 = float(input ('Por favor, me informe o segundo valor: '))

maior_valor = 0

if valor1 > valor2:
    maior_valor = valor1
    print (f'O maior valor entre {valor1} e {valor2} é o primeiro valor: {maior_valor}')
elif valor2 > valor1:
    maior_valor = valor2
    print (f'O maior valor entre {valor1} e {valor2} é o segundo valor: {maior_valor}')
else:
    print ('Os valores são iguais')
