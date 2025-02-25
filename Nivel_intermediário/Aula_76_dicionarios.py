# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

#na lista vc tem os indices que são adicionados automaticamente, aqui não
#nos dicionários vc não tem indices mas sim chaves, que são valores imutaveis que vc devine para referenciar algumas coisa
#voce tem que indicar o que esta sendo referenciado, aqui vc basicamente cria os indices mas podendo escolher como chama-los

'''PRIMEIRA FORMA DE ESCREVER'''
# pessoa = dict (
#     nome = 'Daniel',
#     sobrenome = 'Fernandes',
#     idade = 21,
#     altura = 1.75,
#     endereco = [
#         dict(rua = 'Urandi', numero = 312,),
#         dict(rua = 'Outra rua', numero = 'Outro numero')
#     ]
# )

'''OUTRA FORMA, MAIS COMUM'''
pessoa = {
    'nome': 'Daniel',
    'sobrenome': 'Fernandes',
    'idade': 21,
    'altura': 1.75,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}
#voce não deve ter chaves repetidas, se não vai ser considerado o valor da ultima que esta repetida
print (pessoa['nome'])
print (pessoa ['idade'])

print ()

for chaves in pessoa:
    print (f'{chaves} : {pessoa[chaves]}')


'''DICIONARIOS SÃO USADOS PARA LISTAR COISAS QUE TEM MAIS DE UM ATRIBUTO'''