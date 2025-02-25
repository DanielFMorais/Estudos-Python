'''
Listas em python
tipo list  -  mutável #lista de coisa
Suporta vários valores de qalquer tipo 
conhecimentos reutilizáveis - indices e fatiamento
métodos úteis - append, insert, pop, del, clear, extend, +

create  read   update    delete
criar   ler    alterar   apagar  = lista[i] (CRUD)
VOCE USA [] PARA CRIAR UMA LISTA 

evite mover indices da lista, se vc for adicionar ou deletar, faça isso do final dela
'''
#        0    1  2   3
lista = [10, 20, 30, 40]
# lista [2] = 300
# del lista [2]

# print (lista)
# print (lista [2])

######

lista.append(50) #adiciona coisas na lista, vc pode adicionar quantas coisas quiser, essas coisas sempre vão aparecer no final da lista
lista.append(60) 
lista.append(70)
ultimo_valor = lista.pop(3) # ele remove o ultimo item adiconado da lista, no caso aqui iria apagar o 50 da lista
print (lista, 'removido', ultimo_valor)