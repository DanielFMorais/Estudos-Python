#try, except, else, finally

#finally sempre será executado junto com o try, mesmo que ocorra um erro

# try: 
#     print ('Abrir arquivo')
#     8/0
# finally:
#     print ('Fechar arquivo')

'''Você também pode usar o except junto com oo finaly'''

try: 
    print ('Abrir arquivo')
    8/0
except ZeroDivisionError:
    print ('Você dividiu por zero')
else:
    print ('O código não deu erro')#o else, é para quando o código foi totalmente sem erro
finally:
    print ('Fechar arquivo')#vai ser executado não importa o que aconteça

#finally não trata a excessão