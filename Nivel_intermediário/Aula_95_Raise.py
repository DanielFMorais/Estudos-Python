#raise = lançando exceções (erros)

''''
Você usa o raise quando vc quer fazer um erro propositalmente, a utilidade disso aqui varia, mas por exemplo que vc esta trabalhando 
com um try e deu ZeroDivigionError mas vc não quer q o programa fecha, vc faz um except zerodivigionerro e depois manda o programa salvar
o arquivo, mas depois vc manda um raise para o erro ser exibido 
'''
# def divide(n, d):
#     try:
#         return n/d
#     except ZeroDivisionError:
#         print ('Estou salvando o arquivo')
#         raise 

# print (divide(8,0))

'''DICA: SE O NOME DA SUA FUNÇÃO TA DIFICIL PROVAVELMENTE ELA ESTA FAZENDO MAIS COISA DO QUE DEVERIA'''

#criei uma função para falar se esta dividindo por zero, aqui usei o raise para criar um erro
def não_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError ('Você esta tentando dividir por zero')
    return True

#aqui estou criando uma função que determina se o valor do numerador é inteiro ou float
def deve_ser_int_ou_float (n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)): #aqui eu falei que se não for float ou inteiro
        raise TypeError (
            f'"{n}" deve ser do tipo int ou float'
            f'"`{tipo_n.__name__}" eviando'
        )
    return True

def divide (numerador, divisor):
    deve_ser_int_ou_float (numerador)
    não_aceito_zero (divisor)
    return numerador / divisor

print (divide(8,0))