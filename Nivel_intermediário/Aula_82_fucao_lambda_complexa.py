#funções lambdas podem ser a mesma coisa que funções normais, ou seja, podem ter mais de uma função dentro da função, poder receber vairos argumentos, etc


def executa (funcao, *args):
    return funcao(*args)

def soma (x,y):
    return x + y

def criar_multiplicador (multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

#o python fala que vc tem que executar a função, então basicamente vc executa uma função que executa outra, no caso daqui criamos a função executa, que basicamente recebe uma função e retorna
#ela mesma, isso é literalmente so para ativar a função
print(
    executa(
        lambda x, y: x + y, 2 ,3 #aqui vc baicamente definiu os argumentos, depois do dois pontos vc definou o return e depois mostrou os valores
    )
)

#uma função multiplicador agora vamos fazer uma duplicador, ou seja, vamos sempre duplicar um numero 


duplica = executa (
    lambda m: lambda n: m * n,
    2
)

print (duplica (2))
#agora se vc fosse criara uma lambda que soma todos os valores

print (
    executa( 
        lambda *args: sum(args),
        2,2,2,2,2
    )
)