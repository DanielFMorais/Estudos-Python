# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

#crie uma função que fala se um número é par ou ímpar 
#retorne se o númeor é par ou impar

#####

'''EXERCICIO 1'''

def multiplicador (*args):
    total = 1
    for valor in args:
        total *= valor
    return total

multiplicacao = multiplicador(2,2,4)
print (multiplicacao)
print (2*2*4)

print ('#' * 20)

#####

'''EXERCICIO 2'''

def par_impar (valor):
    if valor % 2 == 0:
        return print (f'O {valor} é PAR')
    else:
        return print (f'O {valor} é IMPAR')

valor = int(input('Por favor, me fale um valor: '))
resultado = par_impar (valor)

print (resultado)