texto = 'Python'
#while é mais usado quando não sabemos quantas repetições irão ocorrer

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input (f'Sua senha ({repeticoes}x):')

#     repeticoes += 1

# print (repeticoes)
# print ('Aquele laço poderia ser infinito')


#iteraveis te entregam um valor por vez

'''O for é mais usado quando sabemos a quantidade de repetições que serão feitas, por exemplo, para imprimir um texto na tela vc sabe quantas str tem naquela palavra'''

texto = 'Python'
novo_texto = ''
for letra in texto: #neste caso vc criou a variável letra aqui mesmo
    novo_texto += f'*{letra}'
    print (letra)

print (novo_texto + '*')

