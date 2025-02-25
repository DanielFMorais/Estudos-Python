"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
#parametros vc usa na definição da função 
#argumentos sao os valores referentes ao parametro

def soma(x, y, z):#se vc define 3 valores, vc tem que preencher 3 valores
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)#argumento não nomeado, então é feito na ordem, por isso é chamado argumento posicional
soma(1, y=2, z=5) #isso é parametro nomeados onde vc basicamente nomeia os parametros que vc deseja chamaar
 #se vc nomear um argumento, todos os argumentos que vem depois dele devem ser nomeados tamb
 #geralmente vc deve chamar todos nomeados ou todos não nomeados geralmente 

print(1, 2, 3, sep='-')
