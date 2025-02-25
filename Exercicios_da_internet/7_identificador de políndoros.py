#Crie um script capaz de detectar palíndromos. 
#Um palíndromo é uma palavra que permanece a mesma se for lida de trás para frente, como “arara” ou “radar”.

# polindromo = 'arara'

# polindromo_invertido = polindromo[::-1]

# if polindromo_invertido == polindromo:
#     print ('Isto é um políndromo!')
# else:
#     print ('Isto NÃO é um políndromo')

#verção altomatizada com o cliente oferecendo

entrada = input ('Por favor, me informe uma palavra:  ')

palavra_invertida = entrada [::-1]

if palavra_invertida == entrada:
    print (f'A palavra informada: {entrada}, É UM POLÍNDROMO')
else:
    print (f'A palavra informada: {entrada}, NÃO É UM POLÍNDROMO')