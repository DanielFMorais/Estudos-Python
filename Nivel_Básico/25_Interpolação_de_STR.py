'''
Interpolação básica de strings 
s -  string
d e i - int
f - float
x e X - Hecadecimal (ABCDEF0123456789) (usado para converte hexadecimais )
'''

nome = 'Daniel'
preco = 1000.95897643
#varivael = 'daniel, o preço total foi R$ 1000.958' ficaria 
variavel = '%s, o preço total foi de R$%.2f' % (nome, preco)
print (variavel)
print ('O hexadecimal de %d é %04f' % (1500, 1500))