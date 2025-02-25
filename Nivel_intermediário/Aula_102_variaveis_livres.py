#variaveis livres + nonlocal

'''
variaveis livres são variaveis que não são definidas dendro do escopo de uma segunda funçao. mas sim no escopo de uma função externa no caso do closure
'''
#locals mostra todas as variáveis locais
#globals mostra todas as variáveis globais

# def fora(x):
#     a = x

#     def dentro ():
#         return a #aqui por exemplo, ela não é definida aqui, mas sim fora deste escopo ali encima
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print (dentro1())
# print (dentro2())

def concatenar (string_inicial):
    valor_final = string_inicial

    def interna (valor_a_concatenar):
        nonlocal valor_final #isso mostra que a variável não é deste escopo e que deve procurar a variável no escopo acima 
        #isso basicamente deixa a variável ser atualizada na funçao interna
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar ('a')
print (c('b'))
print (c('c'))
print (c('s'))

final = c()

print (final)
###############

"""
Ex1)
--UNBOUND VARIABLES ou FREE VARIABLES (VARIÁVEIS LIVRES)
"""

def funcao_exterior():
    x = 10
    
    def funcao_interna():
        print(x)  # Referencia a variável x, que é uma variável livre, aqui só posso fazer a referência, se tentar alterar a variavel livre ocorrerá um erro
        
    funcao_interna()

funcao_exterior()  # Executando a função

# out:
10


"""
Ex1.1)
--UNBOUND VARIABLES ou FREE VARIABLES (VARIÁVEIS LIVRES)
"""

def funcao_exterior():
    x = 10

    def funcao_interna():
        x += 5  # Aqui estou tentado alterar a variável x
        print(x)

    funcao_interna()


funcao_exterior()  # Ao executar ocorrerá o erro UnboundLocalError

# out:
#UnboundLocalError: cannot access local variable 'x' where it is not associated with a value]



"""
Ex2)
--NONLOCAL
Como alterar as unbound variables dentro de funções internas:
"""

def funcao_exterior():
    x = 10

    def funcao_interna():
        nonlocal x  # definindo 'x' como nonlocal
        x += 5  # agora sendo nonlocal posso alterar
        print("Valor de x dentro da função interna:", x)

    funcao_interna()
    print("Valor de x fora da função interna:", x)


funcao_exterior()  # executando a função

# out:
# Valor de x dentro da função interna: 15
# Valor de x fora da função interna: 15


"""
Ex3)
--GLOBAL
"""

x = 10  # Variável global, definida no escopo global do programa

def funcao():
    global x  # Declarando o uso da variável global dentro da função, agora posso altera-la no escopo da função.
    x += 5
    print("Valor de x dentro da função:", x)

print("Valor de x antes da função:", x)

funcao()  # executando a função
print("Valor de x após a função:", x)

# out:
# Valor de x antes da função: 10
# Valor de x dentro da função: 15
# Valor de x após a função: 15