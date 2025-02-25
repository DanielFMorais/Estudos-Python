#Peça ao usuário para inserir três números e calcule a média deles.

valor1 = int(input ('Por favor, me informe o primeiro valor: '))
valor2 = int(input ('Por favor, me informe o segundo  valor: '))
valor3 = int(input ('Por favor, me informe o terceiro  valor: '))

media = (valor1 + valor2 + valor3) / 3

print (f'A media dos valores informados = {media:.2f}')
