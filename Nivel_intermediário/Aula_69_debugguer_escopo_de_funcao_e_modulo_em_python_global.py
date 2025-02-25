"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
   # global x #ISSO PERMITE A VARIÁVEL GLOBAL SER AUTERADO NO ESCOPLO INTERNO MAS É UMA MÁ PRATICA DE PROGRAMAÇÃO
    x = 10

    def outra_funcao():
        #global x
        x = 11#SE NÃO EXISTISSE ESTE X AQUI, O X DESTA FUNÇÃO SERIA DO ESCOPO EXTERNO MAIS PROXIMO
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)