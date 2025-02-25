"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input ('Por favor, digite um numero inteiro: ')

try:
    numero_inteiro = int(numero)

    if numero_inteiro % 2 == 0:
        print (f'O número {numero} é um número PAR')
    else:
        print (f'O número {numero} é um número IMPAR')
except:
    print ('Você não digitou um número inteiro')

# na correção poderiamos ter usado o comendao isdigit que fala se o numero é inteiro, ai vc não iria preciar usar o try mas daria o mesmo resultado

if numero.isdigit():
    numero_inteiro = int(numero)

    if numero_inteiro % 2 == 0:
        print (f'O número {numero} é um número PAR')
    else:
        print (f'O número {numero} é um número IMPAR')
else:
    print ('Você não digitou um número inteiro')