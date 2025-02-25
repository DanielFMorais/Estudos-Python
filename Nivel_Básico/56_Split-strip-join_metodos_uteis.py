'''
split e join com list e str

split - divide uma string

join - une uma string
'''

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split() #se vc não colocar nada do paragrafo ele vai separar a cada espaço que ele achar
print (lista_palavras)

###

lista_frases = frase.split(',')#ai ele vai separar na virgula, ocasionalmente ela não vai aparecer
print (lista_frases)

###
frase = 'Olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate (lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip)

# print (lista_frases_cruas)
# print (lista_frases)
#METODO OFICIAL DE COMO FAZER PARA SEPARAR CADA ITEM



frases_unidas = ', '.join(lista_frases) #tem que ser valores iteravies

print (frases_unidas)