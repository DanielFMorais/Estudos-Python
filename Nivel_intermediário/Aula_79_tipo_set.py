
# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Daniel') #set retorna iteravies, então se vc mandar uma str ele vai separar cada unidade dela e ela não garante a ordem
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # ele também pode ser escrito assim, se vc mandar mais de um valor ai sim que ele vai mandar a str inteira
# print (s1)

''''''

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;

s1 = {1, 2, 3, 3, 3, 3, 3, 4} #o set remove valores duplicados naturalmente
print (s1)

'''Se você tiver, uma lista por exemplo que quer eliminar os valores duplicados, uma forma de fazer isso é usando set'''
l1 = [1, 2, 3, 3, 3, 3, 3, 3, 4, 5]
s1 = set(l1)
l2 = list (s1)
print (l2) #lembrando que ele não garante a ordem

# - Não aceitam valores mutáveis;
#s1 = set(1, 2, 3, [1,2,3]) #isso aqui vai dar erro pois ele não aceita valores mutaveis dentro dele, ou seja
'''listas, dicionários e set'''


# - não tem índexes, ou seja, eles não podem ser consutados por indices que nem os outros tipos;
# - não garantem ordem;

# - são iteráveis (for, in, not in)
#eles são iteraveis ou seja, vc pode usar metodos nele

s2 = {1, 2, 3}
print (4 in s2) #retorna falso, já que não ta la, é desta forma que vc verifica se ele tem um valor
for numero in s2:
    print (numero)


##################

print ('########################')

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Daniel')#se mandar assim ai vai inteiro
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4,))#assim vc vai poder colocar varios valores mas lembre-se de colocar entre conchetes
'''para poder ir como iteravie '''
#s1.clear() vai basicamente limpar o set
s1.discard('Olá mundo') #aqui vc basicamente descarta o que vc colocar dentro dos parenteses, aqui vc pode colocar literalmente o que vc quer descartar
print(s1)



####################################

print ('########################')

# Operadores úteis:

'''PENSA NISSO AQUI COMO AQUELE TREIM DE MATEMATICA, AS OPERAÇÕES MESMO, INTERCESSÃO, UINIÃO E TAL '''
# união | união (union) - Une \\\\ simbulo = |
# intersecção & (intersection) - Itens presentes em ambos \\\ simbulo = &
# diferença - Itens presentes apenas no set da esquerda \\\\ simbulo = -
# diferença simétrica ^ - Itens que não estão em ambos \\\\ simbulo = ^

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2

print (s3)
print (s4)
print (s5)
print (s6)