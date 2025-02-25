'''
crie uma função que retorna uma letra do alfabeto, dado o seu índice. Por exemplo, 
o índice 1 deve retornar a letra "A", o índice 2 deve retornar a letra "B" e assim por diante. 
Caso o índice esteja acima ou abaixo dos limites do alfabeto, a função deve retornar um string vazio.

'''
alfabeto = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def indentificador_alfabeto (indice):
    if indice < 1:
        print(f'Não existe esta letra no alfabeto, Primeira letra disponível é "A" indice 1 ')
    if indice > 26:
        print (f'Letra não no alfabeto, letra máxima é "z" indice 26')
    else:
        return alfabeto[indice]

print(indentificador_alfabeto(99))
