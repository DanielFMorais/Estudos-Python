#Escreva um programa que peça ao usuário um número inteiro e calcule o fatorial dele. 

valor = int(input('Por favor, me informe um número inteiro: '))

fatorial = 1 
for i in range(valor, 0, -1):
    fatorial *= i

print (fatorial)

