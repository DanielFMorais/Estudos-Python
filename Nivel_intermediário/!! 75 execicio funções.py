# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicador (multiplicador):
    def multiplicar (numero):
        return numero * multiplicador
    return multiplicar 

duplicar = multiplicador (2)
triplicar = multiplicador (3)
quadruplicar = multiplicador (4)

print (duplicar (2))
