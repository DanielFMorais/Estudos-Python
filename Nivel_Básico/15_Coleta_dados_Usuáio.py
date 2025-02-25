#usamos o comando input, que gera um resultado sempre do tipo str, por isso a importancia de saber fazer a conversão de tipos

'''
se vc colocar um = na frente da variável que vc esta vendo no código, retornara o nome da variavel em si,
por exemplo, se vc colocar nome = input('qual o seu nome?') quando vc realizar o comando print (f'o seu nome é {nome}) somente vai aparecer o resultado do nome que a pessoa colocar
mas caso vc coloque print (f'o seu nome é {nome=}) vai aparecer "o seu nome é nome= daniel", viu que neste caso mostrou que o nome da variavel que esta puxando é a varivavel nome
'''

# nome = input('Qual o seu nome? ')
# print(f'O seu nome é: {nome}')

numero1 = input ('Digite um número: ')
numero2 = input ('Digite outro número: ')

print (f'A soma de {numero1} e de {numero2} = {int(numero1) + int(numero2)}')