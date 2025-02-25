#Crie um programa que converta uma temperatura dada em Celsius para Fahrenheit. 

print ('Vamos começar a converter de °c para °F')
valor = float(input('Por favor, me fale a temperatura para converter: '))

conversao = valor * (9/5) + 32

print (f'O valor da conversao = {conversao} °F')