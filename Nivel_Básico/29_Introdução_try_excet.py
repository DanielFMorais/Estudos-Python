'''
Introdução ao try/except
try -> Tentar executar o código
except -> Ocorreu algum erro ao tentar executar

isso é util que ao inves de parar o código, você faz como se fosse um if enquanto o código funcione, no caso de algum erro ele vai para o except
'''

numero_str = input ('Vou dobrar o número que você digitar: ')

print (numero_str.isdigit()) # O isdigit informa se o usuário colocou somente numero literalmente somente numeros, pontos e virgulas fazem a verificação ficar false 

# if numero_str.isdigit():
#     numero_float = float (numero_str)
#     print (f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print ('Você não digitou somente numeros')

try:
    print ('STR:', numero_str)
    numero_float = float (numero_str)
    print ('FLOAT:', numero_float)
    print (f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print ('Você não digitou somente numeros')