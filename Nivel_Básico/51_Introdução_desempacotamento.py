'''
introdução ao desempacotamento + tuples (tuplas)
'''


lista = ['Maria', 'Carol', 'Daniel']
nome1, nome2, nome3 = lista
print (nome1)
print (nome2)
print (nome3)
#aqui vc basicamente esta criando uma variavel para cada item da lista em ordem da esquerda para a direita
#NESTE CASO AQUI VC NÃO PODE TER MAIS OU MENOS VARIÁVEIS QUE OS ITENS DENTRO DA LISTA, O QUE LIMITA MUITO a n ser que seja uma unica variável para tudo 

'''
para você corrigir este problema, você tem que determinar o que vai fazer com o resto, e para isso vc usa a seguinte regra
'''

lista = ['Maria', 'Daniel', 'Carol']
nome1, *_ = lista #é uma convenção no mundo do python que qualquer variável que por mais que exista não seja utilizada ser chamda de _
print ('######')
print (nome1)
#aqui você basicamente definiu uma outra lista chamada resto, que pega todos os outros valores 
print (_)

'''
Para você pegar valores sem ser o primeiro, vc basta criar outra variável nula antes do valor 
'''

lista = ['Maria', 'Daniel', 'Carol']
_, nome2, *_ = lista
print ('#####')
print (nome2)

''''
O terceiro valor a mesma coisa
'''
lista = ['Maria', 'Daniel', 'Carol']
_, _, nome3, *_ = lista #de qualquer forma é recomendavel utilizar a variável de resto
print ('#####')
print (nome3)


