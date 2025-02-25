# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))


# def generator (n=0):
#     yield 1 #pausar
#      #toda função que tem yield é uma generator functions 
#     #o yield informa que vc vai pausar naquela função até que venha o next
#     print ('coninuando...')
#     yield 2 #pausar 
#     print ('continuando de novo...')
#     yield 3
#     print ('vou terminar ')
#     return 'ACABOU'

'''
entaõ ele vai mostrar o primeiro yield e depois ele vai pausar, e parará a função até que eu execute o proximo next
fazendo com que ele volte a executar o que esta a frente, ou seja, so no segundo next que vai aparecer o continuando 
'''

# gen = generator (n=0)
# print (next(gen))
# print (next(gen))
# print (next(gen))
# #esta é a forma manual, mas tem com automatizar 

# for n in gen:
#     print (n)
# #forma automatica

''''''''''''''''''''''''''''''#como fazer para fazer um range por exemplo 

def generator(n=0, maximum=10):
    while True:
        yield n #protege o wuile já que ele pausa
        n += 1

        if n > maximum:
            return


gen = generator(maximum=15)
for n in gen:
    print(n)