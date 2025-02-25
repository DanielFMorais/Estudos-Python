'''
Formatação básica de strings
s - string
d - int
f - float
. <número de dígitos> f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda 
< - direita                     FAZ COM QUE DETERMINADA QUANTIDADE DE CARACTERES SEJA PREENCHIDA NO TERMINAL
^ - centro
= - força o numero a aparecer antes dos zeros
sinal - + ou -
ex: 0 > -100, .1f
conversion flags - !r !s !a
'''

variavel = 'ABC'
print (f'{variavel}.')
print (f'{variavel: >10}.')
print (f'{variavel: <10}.')
print (f'{variavel: ^10}.') #Você pode colocar qualquer caractere antes do sinal <>^ que o espaço será preenchido por aquele caractere
print (f'{variavel:-^10}.')
print (f'{variavel:-<10}.')
print (f'{variavel:->10}.')

print()
print(f'{1000.12341234:.1f}')
print(f'{1000.12341234:,.1f}')#se você colocar uma virgula antes do .f1 por exemplo. o numero vai ser separado suas centanas por ,
print(f'{1000.12341234:+,.1f}')#Se vc colocar um sinal de mais ou de menos logo depois dos dois pontos, vai significar que é pro python mostrar o sinal independente ser for positivo ou negativo
print(f'{-1000.12341234:-,.1f}')
print(f'{-1000.12341234:0=+10,.1f}')

print()
print(f'O hexadecimal de 1500 é {1500:08x}')
