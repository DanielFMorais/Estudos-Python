# Métodos úteis dos dicionários em Python

# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
#update - Cria e atualiza chaves

pessoa = {
    'nome': 'Daniel',
    'sobrenome': 'Fernandes',
}

#####       len     #####

#print (pessoa.__len__())
print (len(pessoa)) #informa quantoas chves tem 
'''É A MESMA COISA, USA O LEN() QUE É MAIS FACIL, COMPLICA MINHA VIDA NÃO'''


######      keys    ####
print ()
print ('**' * 10)

print (tuple(pessoa.keys())) #informa quais chaves tem

#se vc quiser deixar elas aparecendo como uma lista mesmo pode usar 
for chave in pessoa.keys():
    print(chave)

######     values   #####
print()
print ('**' * 10)

print (list(pessoa.values())) #informa o que esta condido nas chaves

for valor in pessoa.values():
    print(valor)

#####       items   ######


print()
print ('**' * 10)

print (list(pessoa.items())) #infoma as chaves e seus valores

for chave, valor in pessoa.items():
    print (chave, valor)

#####       setdefault   ######

print()
print ('**' * 10)

pessoa.setdefault('idade', 0) #determina um valor padrão caso eu não tenha aquela chave cadastrada 
#se a cahve existir simplesmente não vai acontecer nada

print (pessoa['idade'])


### shallow copy - copy ###

d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0, 1, 2],
}

# d2 = d1

# d2['c1'] = 1000
# print (d1) #quando vc faz isso ate mesmo o valor de d1 é modificado, pois vc esta auterando um valor de um dicionário igual ao outro, ou seja, tome cuidado
# por isso temos que usar a função copy, para copiar o dicionário mas sem modificar o primeiro dicionário
import copy

d2 = d1.copy() #copia tudo que for imutavel, mas se tiver uma lista por exemplo, ele somente vai linkar ela, ou seja acontece o mesmo problema daqui de cima
d2['c1'] = 1000
d2['l1'][1] = 99999
print()
print ('**' * 10)
print (d1)
print (d2)

'''para resolver este problema, temos que importar uma função chamada copy pra assim fazer a copia mais profunda'''


# d2 = copy.deepcopy(d1) #ai assim eu farei uma copia profunda, ate mesmo pegando os valores que estão dentro dos mutaveis
# print (d1)
# print (d2)


### get ###

p1 = {
    'nome': 'Daniel', 
    "sobrenome": 'Fernandes'
}

print()
print ('**' * 10)
print (p1.get('nome', 'Não existe')) #vai retornar o valor daquela chave, depois da virgula vc coloca o que aparecer caso não tenha aquilo na lista


### pop ###

p1 = {
    'nome': 'Daniel', 
    "sobrenome": 'Fernandes'
}

nome = p1.pop ('nome') #retorna o valor de nome, mas apaga a chave logo em seguida
print()
print ('**' * 10)
print (nome)
print (p1)


### PopItem ###

p1 = {
    'nome': 'Daniel', 
    "sobrenome": 'Fernandes'
}

ultima_chave = p1.popitem #Remove a ultima chave
print ('**' * 10)
print (ultima_chave)
print (p1)

### Update ###

print()
print ('**' * 10)
# p1.update({
#     'nome' : 'novo valor',
#     'idade' : 21,
# })
p1.update(
    nome = 'Novo nome',
    idade = 30,
)
print (p1)