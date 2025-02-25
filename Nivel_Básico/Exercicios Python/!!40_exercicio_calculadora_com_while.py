'''Calculadora com while'''

while True:

    numero1 = input ('Por favor, me informe o primeiro número:  ')
    numero2 = input ('Por favor, me informe o segundo número:  ')
    operador = input ('Por favor, informe o operador matemático [+-*/]:  ')
    
    operadores_validos = '+-*/'
    numeros_validos = None
    num1_float = 0
    num2_float = 0
    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos  = None
    

    if numeros_validos is None: 
        print ('Um ou ambos os numeros digitados não são validos')
        continue

    if operador not in operadores_validos:
        print ('Operador invávlido')
        continue

    if len(operador) > 1:
        print ('Digite somente um operador')
        continue
    
    print ('Realizando calculos... pro favor verifique os resultados abaixo:')
    if operador == '+':
        print (f'{num1_float}+{num2_float}=', num1_float + num2_float)
    elif operador == '-':
        print (f'{num1_float}-{num2_float}=', num1_float - num2_float)
    elif operador == '*':
        print (f'{num1_float}*{num2_float}=', num1_float * num2_float)
    elif operador == '/':
        print (f'{num1_float}/{num2_float}=', num1_float / num2_float)

    sair = input('Você deseja sair? ').lower().startswith('s')
    if sair is True:
        break