"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
# o que esta dentro da função fica na função, é como se fosse um universo paralelo individual 



# def escopo ():
#     x =1 
#     print (X)

# print (x)
# escopo 
# vc não consegue manipular coisas de dentro da função fora da função, a função basicamente é um procedimento e pra vc modificar ele vc deve modificar la dentro
#vc basicamente usa a função para puxar uma serie de comando por isso vc não pode modificar ela fora dela mesma 


x = 1 #escoplo gobal 

def escopo():
    #global x não faz isso aqui não para facilitar
    #a palavra global faz uma variável do escopo externo ser amesma no escopo interno
    x = 10 #escoplo local

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

#vc não pode acessar variaveis de escopos interternos somente externos, então no caso da outra função ela pode sim acessar a variável x, mas a função escopo não pode acessar a variavel y

print(x)
escopo()
print(x)