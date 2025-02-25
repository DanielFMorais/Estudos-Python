# Operadores lógicos 
# and (e) or (or) not (não)
# and - todoso as condições precisam ser verdadeiras 
# se qualquer valor for considerado falso a expressão inteira será avaliada como falsa e naquele valor em falso especifico, não verificando os a frente
# são conisderados falsy (que vc já viu )
# 0 0.0 '' false ou seja, valores falsos são o zero, o zero ponto zero e aspas vazias
# Também existe o tipo None que é usado para representar um não valor (basicamente não existe)

entrada = input ('[E]ntrar [S]air  ')
senha_digitada = input ('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_permitida == senha_digitada:
    print('Entrar')
else:
    print('Sair')

#avaliação de curto-circuito
print (True and False and True)
print (bool(0)) #false
print (bool(0.0)) #false
print (bool('')) #false
print (True and 0  and True) # ele para no zero pois zero é falso e retorna o valor de zero em especifico.