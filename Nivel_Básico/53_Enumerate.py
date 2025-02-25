'''
Enumerate = ele basicamente enumera iteraveis (indices)
'''

lista = ['Maria', 'Carol', 'Daniel']
lista.append ('Fernandes')

'''
vc basicamente tem um comando para determinar os indices que estão em cada parte da lista
'''
### forma que vc ve o local da memoria 
lista_enumerada = enumerate(lista)
print (next (lista_enumerada)) #é importante colcoar o next, pois se não ele vai dar o valor da memoria dele, onde esta alcoado

### forma que vc vé normal
for item in enumerate(lista): #vc geralmente coloca ele aqui para não poder fazer somente uma vez, já que se vc olocar ele na variável mesmo ele so vai ser usado uma unica vez
    print (item)
    
###outra forma de ver é simplesmente transformando o tipo do enumerator para ou list ou tuple 

lista_enumerada = list(enumerate(lista))
print (lista_enumerada)

#da para fazer empacotamento 

###MELHOR JEITO DE USAR
for indice, nome in enumerate(lista): #é a mesma coisa do dali de cima
    print (indice, nome)