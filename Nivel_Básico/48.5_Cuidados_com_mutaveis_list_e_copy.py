'''
Cuidados com dados mutáveis

= - copiado o valor (imutáveis)
= - Aponta para o mesmo valor na memória (mutável)
'''

# nome = 'Luiz'
# noutra_variavel = nome
# nome = 'João'
# print (nome)
# print (noutra_variavel)
# #fazer isso aqui é possivel porq ele le de cima para baixo, então antes mesmo de a primeira variavel nome ser excluida ela já estava em outra variável

# lista_a = ['Daniel', 'Carol']
# lista_b = lista_a

# lista_a [0] = 'Qualquer coisa'

# print (lista_b)
# #neste caso aqui estou fazendo com que tanto a lista a e b puxem o mesmo valor


lista_a = ['Daniel', 'Carol']
lista_b = lista_a.copy()#agora eu estou copiando a lista a mas agora se eu modificar a lista a não vai modificar a lista b pois eu fiz e copia e cola gerando um outra variável totalmente
#independente gerando outra lista
lista_a[0] = 'qualquer coisa'
print (lista_a)
print (lista_b)