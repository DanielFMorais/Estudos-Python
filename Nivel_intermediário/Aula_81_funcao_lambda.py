# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [1, 2, 3, 4, 5, 64, 14, 4]

# lista.sort() #ordena de froma crescente 
# lista.sort(reverse=True) #ordena de forma decrescente

# #sorted(lista) mesma coisa mas faz uma copia rasa

# print (lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#o python não consegue ordenar dicionários, ou seja, ele não consegue usar o sort nas chaves
#aqui temos uma função que ordena a lista, mas para isso vc tem que criar 

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena ) #key é uma definição de função
# #MANEIRA CONVENCIONAL

#USANDO LAMBIDA
# lista.sort(key=lambda item: item['nome']) #É a mesma função, so que escrita em uma unica linha e nao tem nome, é como se vc criasse uam função para aquele momento

# for item in lista:
#     print (item)

#se você quisesse fazer uma nova lista com as ordenações,  é so usar o serted que mosramos ali encima 

def exibir (lista):
    for item in lista: 
        print(item)
    print()

l1 = sorted (lista, key= lambda item: item ['nome'])
l2 = sorted (lista, key=lambda item: item ['sobrenome'])

exibir (l1)#lembrando que isso aqui são copias rasas ou seja, não copiam mutaveis que estão dentro
exibir (l2)