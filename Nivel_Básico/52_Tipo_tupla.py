'''
Tipo tupla == uma lista imutável

é uma lista mas com valor imutavel , ou seja, não da para modificar ela, so isso... kkk

'''

tuples = 'Maria', 'Daniel', 'Carol' #para criar uma tuple basta colocar os valores sem os conchetes

print (tuples)
print (tuples [-1])

"""Outra forma de escrever tuple"""

tuples = ('Maria', 'Daniel', 'Carol')

print (tuples)
print (tuples [1])

'''da para vc transformar listas em tuple'''

lista = ['Maria', 'Daniel', 'Carol']
tuples = tuple(lista)

print (tuples)
print (tuples [0])