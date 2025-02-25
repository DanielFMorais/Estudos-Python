"""
Retorno de valores das funções (return)
"""

'''
existem funções que retornam ações que é o caso do print e ações que retornam valores, no caso que retornam ações, vc não tem valores, então basicamente vc quer uma ação mesmo 
no caso das que retornam valores, vc quer o valor que aquela função retorna 
'''

'''
se vc usa a função return vc basicamente fala que o valor qe vem da função pode ir para qualquer lugar, inclusive em variáveis
'''


def soma(x,y):
    if x > 10:
        return 10, 20
    return x + y #o return é exclusivo de funções e metodos, então ele só vai existir em funções que é o caso aqui e em metodos
    #não acontece nada depois do return, ou seja, depois dele o def basicamente fica inutilizavel
    #vc so pode ter um return por função

soma1 = soma(2,2)
soma2 = soma(3,3)
print (soma1)
print (soma2)

print (soma1 + soma2)