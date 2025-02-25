# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
#BASICAMENTE É UMA LISTA COM FUNÇÕES DENTRO 
# o que vem a direita do for é filro, e a esquerda é mapeamento 


# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)

# Mapeamento de dados em list comprehension AQUI VC TEM QUE MANTER O MESMO TAMANHA DA LISTA
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}#aqui vc basicamente nos novos produtos vc criou uma nova lista, onde desempacotando a lista antiga vc pode atualizar ela
    #criando uma nova lista com novos preços por exemplo 
    if produto['preco'] > 20 else {**produto} #aqui vc colocou uma condição na lista que so faça o que esta acima caso o preço for mair que 20, lembrando que tudo que esta a esquerda do 
    #for nas lista é o que vc quer que seja modificado, seguindo a sintaxe -> [o que vc quer que seja executado] for [condição] 
    for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')


#FILTRO EM LIST COMPEHEISON 

# lista = [n for n in range(10) if n < 5] #aqui eu coloquei um filtro para ele adicionar um valor a lista, por tanto que este valor seja menor que 5
# print (lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] * 1.05) > 10
