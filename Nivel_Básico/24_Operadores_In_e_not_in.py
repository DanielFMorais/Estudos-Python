# Operdadores in e not in 
# in significa entre e not in é não esta entre
# strings são iteráveis 
#iteralvel são coisas que podemos navegar item por item
# 0 1 2 3 4 5 
# D a n i e l
#-6-5-4-3-2-1
#vc basicamente consegue rastrear também esse troço, por exemplo no indice 2 que esta a letra n 

nome = 'Daniel'
# print (nome[2])
# print (nome[-4])

print ('a' in nome)
print ('Dan' in nome)
print ('zar' in nome)
print  (10 * '-')
print ('vio' not in nome)
print  (10 * '-')
print  (10 * '-')
print  (10 * '-')

nome = input ('Digite seu nome: ')
encontrar = input ('digite o que você deseja encontrar: ')

if encontrar in nome:
    print (f'{encontrar} esta em {nome}')
else: 
    print (f'{encontrar} não esta em {nome}')