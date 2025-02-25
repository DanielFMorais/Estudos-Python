# from sys import path

# #print (*path, sep= '\n')

# #temos duas formas de importar packs

# import aula99_package.modulo #essa é uma das formas de chamar mas fica muito grande, e lembre-se que somente chamar o pack não ajuda em nada pois ele não executa nada 
# #entoa vc tem que obrigatoriamente chamar o modulo do pack que vc quer

# from aula99_package.modulo import soma #esta é outra forma de chamar o pack, mas aqui vc tem que especificar qual função vc quer dentro do modulo. 

# from aula99_package import modulo #esta é outra forma de fazer que fica no meior termo

# print (soma(2, 2))
# print (aula99_package.modulo.soma(2,2))
# '''Viu é a mesma coisa, so que um é maior que o outro, e ambos tem a mesma desvantagens e vantagens faladas anteriormente'''
# print (modulo.soma(2,2))#é o meio termo entre as duas ali de cima, tanto em vantagens quanto em desvantagens 

'''
vamos supor um cenários, vc esta querendo importar para sua pasta principal "99_introdução" algo daquela parta la encima a aula_99 pack, so que dentro dela vc tem 2 modulos, o modulo normal e 
o modulo b, se vc fizer um import do modulo b no modulo a, ele vai dar erro quando vc tentar chamar ele aqui, pois vc não pode simplesmente chamar como se ele fosse somente de lá se vc 
sabe que vc vai usar ele em outro lugar, você sempre deve pensar no seu main como o principal, ou seja, vc deve sempre pensar no seu programa basico, as pastas subsequentes vc n pode pensar 
como se ela fossem proprias, elas na vdd trabalham para o main
# '''
# from aula99_package.modulo_a import fala_oi, soma

# fala_oi()


'''
FALAREMOS AGORA DO __INIT__ A FORMA DE INICIALIZAÇÃO DO PACKAGE

Basicamente ele é inicialização, vc coloca ele primeiro e ele vai sempre executar primeiramene no package, assim vc pode meio que burla o python, e faz com que ele aceite usar
funções de modulo no package, por tanto que esteja as funções no __init__

para isso vc deve criar uma pasta que se chama __init__.py, isso é obrigatorio
'''

import aula99_package

print (aula99_package.dobra)


# '''
# o init então basicamente executa iicialmente em tudo, o que faz o package parecer um modulo, pode ser muito útil e assim vc não precisa ficar importanto todos subniveis do package 
# LEMBRANDO QUE AQUI É A UNICA HORA QUE VC PODE USAR O IMPORTA * JÁ QUE VC REAOLMENTE QUER ATUALIZAR TODA HORA QUE MUDAR LA MAS SO LA NO INIT
# '''

# print (aula99_package.nova_variavel)
# print (aula99_package.soma(2, 2))
#lembrando que as vantagens e desvantagens de não ficar falando de onde vem é a mesma, aqui ta bagunçado mas com o tempo vc vai entender