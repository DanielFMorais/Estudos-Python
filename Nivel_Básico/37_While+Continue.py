'''
repetições 
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> é quando um código não tem fim

você tem duas formas de quebrar o laço da função while, ou quebrando o laço com comando break ou fazendo que a condição dela exisitr se torne false

o termo CONTINUE faz com que o laço do while seja cortado voltando de volta ao while no inicio, enquanto o break quebra o laço e pula para fora dele, o continue faz com que volte ao inicio do laço
'''

contador = 0

while contador < 100:
    contador += 1
    
    if contador == 10: 
        print('não vou mostrar o 10')
        continue #isso faz com que ele pule esta parte no caso aqui o numero 10

    if contador >= 15 and contador <= 30:
        print('Não vou mostrar o', contador)
        continue #basicamente ele quando chega no continue volta pro inico so isso

    print (contador)


    if contador == 40:
        break

print ('Fim')