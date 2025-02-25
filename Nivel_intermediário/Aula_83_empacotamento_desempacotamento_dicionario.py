# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


# a, b = pessoa
# print (a, b)#assim vc desempacota somente as chaves

# a, b = pessoa.values()
# print (a, b) #assim vc desempacota os valores das chaves

# a, b = pessoa.items()
# print (a, b) #assim vc desempacota uma tupla contendo tanto as chaves quanto os valores

# #vc também pode desempacotar itens internos, é so criar mais variáveis

# (a1, a2), (b1, b2) = pessoa.items()
# print (a1, a2)
# print (b1, b2)

#empacotamento de dicionários

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade' : 21,
    'altura' : 1.5
}

pessoa_completa = {**pessoa, **dados_pessoa}#lembrando que o ** é para extrair os dados do dicionário, e assim vc acaba de criar outro dicionário com os valores de todos os antigos

print (pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)