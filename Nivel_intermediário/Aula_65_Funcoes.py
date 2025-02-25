'''
Introdução ás funções (def) em Python
funções são trechos de código usados para replicar, determinar acão ao londo do seu código. 
Eleas podem receber valroes para parâmetros (argumentos) e reornar um valor específico
por padrão, funções python retornam None (nada)
'''

# def Print(a,b,c):  #começamos com um def e depois colocamos o nome da função e não podemos esquecer dos parenteses 
#     print ('Várias1')
#     print ('Várias2')
#     print ('Várias3')
#     print ('Várias4')
# #usada para não ficar repitindo varias coisas no meio do código, funções são basicamente procedimentos pré estabelecidos
# Print()

# def imprimir(a,b,c): # para vc executar vc tem que colocar os parenteses, oq esta dentro dos conchetes sao basicamente variaveis em parametros
#     print ('Várias1')
#     print ('Várias2')
#     print ('Várias3')
#     print ('Várias4')

# imprimir (1, 2, 3)#voce define os valores dos argumentos aqui onde chamamos argumentos
# imprimir (1, 2, 3)#vc sempre coloca na ordem

# def saudacao (nome):
#     print (f'Olá {nome}')

# saudacao ('Daniel Fernandes')
# saudacao ('Daniel')#vc basicamente pode fazer um código que se atualiza automaticamente com o que vc colocar sem ter que ficas escrevendo muitos códigos 
# no caso aqui, toda vez que chamar a função saudação eu defino o valor da variável nome, no próprio chamado

#você também pode determinar ficar sem valor e caso não for atribuido um valor ele basicamente usa aquilo

def saudacao (nome = 'Sem nome'):
    print (f'Olá {nome}')

saudacao ('Daniel')
saudacao()