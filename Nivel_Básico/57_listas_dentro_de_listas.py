"""
Lista de listas e seus índices
"""
salas = [['Maria', 'Helena'],['Elaine'], ['Luiz', 'João', 'Eduarda', (0,10,20,30,40)]]
#basicamente aqui vc tem que saber como buscar valores dentro de valores, se vc parar para pensaer vai ser assim 
#cada lita tem um indice e dentro dessa lista tem outr indice, então caso vc queria o sla, maria, maira ta na lista indice 0 e maria é o 0
# se fosse a helena sera a lista indice 0 e o item indice 2 helena

print (salas [2][0]) #basicamente vc colocar primeiro o indice da lista que vc esta querendo e depois o intem que esta dentro desta lista 

print (salas [0][1])

print (salas [2][2])

print (salas [2][3][2])#é sempre indo mais a dentro como se fosse camadas

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

#isso aqui mostra que ate mesmo no for, é so vc ir indo camadas mais fundos camada por camada, pense em lista dentro de listas como camadas

