# if / elif / else
#se / se não se/  se não
# else é sempre o contrario de if e ele é sempre o ultimo a ser utilizado então se no codigo tiver um elif ele sera no meio 
#caso vc quiera deixar o código para depois use 3 pontinhos ...

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = False



# if condicao1:
#     print ('Este é o código if')
# else:
#     print ('Este é o código else do primeiro if')

if condicao1:
    print('Este é o if da condição 1')
elif condicao2:
    print('Este é o elif da condição 2')
elif condicao3:
    print('este é o elif da condição 3')
elif condicao4:
    print('Este é o elif da condição 4')
else:
    print('Nenhuma das opções então o else aparece')

# a partir do momento que ele encontra uma unica verdadeira ele já para os blocos e executa so o primeiro verdadeiro encontrado de cima para baixo
# ou seja, se vc quisesse que cada uma das variáveis fosse verificada como unidade vc teria que fazer varios if

if 10 == 10: 
    print('outro if')


print('Fora do if e do else')