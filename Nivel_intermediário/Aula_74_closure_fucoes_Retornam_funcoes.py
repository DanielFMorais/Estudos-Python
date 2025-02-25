"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

'''
aqui vc basicamente criou uma função base e depois colocou outra função dentro dela, falar bom dia aqui vai ser uma função definida
e o nome da pessoa vai ser outra função. isso mostra que vc pode atrasar o funcionamento de alguma função especifica ou automatizar ela
'''
'''

Em Python, um closure é tipicamente uma função definida dentro de outra função. Esta função interna pega os objetos definidos em seu escopo
 envolvente e os associa ao próprio objeto de função interna. A combinação resultante é chamada de closure. Closures são um recurso comum em linguagens de programação funcional
'''