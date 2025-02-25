#Crie um programa que mostre a tabuada de um número fornecido pelo usuário.

valor_tabuada = int(input('Por favor, deseja a tabuada de qual número ?  '))

for i in range(1,11):
    print (f'{valor_tabuada} x {i} = {valor_tabuada * i}')