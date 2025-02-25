
"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)


'''
basicamente aqui fala que vc pode usar funções em funções e vc pode usar funções em argumentos,
vc basixamente pode fazer qualquer coisa com funções que nem outros tipos de dados

'''