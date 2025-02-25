#generator expression, iterables e iterators em python


#generator são funções que sabem pausar em determinada ocasião 
#todo generator é um iterater pois vc pode fazer for nele, entre outras coisas que da para fazer com iterator
#contudo o iterator não é como o generator


iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
#generator = [n for n in range(10)] #eu sei que vc não entendeu daniel, mas isso aque é o conceito de list compeheison, uma lista com um for dentro
generator = (n for n in range(10)) 
#aqui que vem o jump of the cat, generator é basixamente um list compeheidon em formato tuple ou seja um tuple compeheison formando uma generator expression
print (generator)#ele tem a grande vantagem de so te mostrar quando vc pede economizando espaço na memória

'''
Agora okay, ele esta salvo mas e como eu faço para mostrar ele? simples a função next como no iterator
'''

# print (next(generator))
# print (next(generator))
# print (next(generator))
# print (next(generator))
# print (next(generator))
'''ou para ser automatico '''

for n in generator:
    print (n)
'''
AGORA VANTAGENS E DESVANTAGENS DA LISTA E DO GENERATOT

LISTA == pode ser acessada rapidamento por indicies já que está totalmente armazenada na momoria mas em contra partida é mais pesado pois esta tudo salvo, ou seja
é mais rapida mas é mais pesada

generator == É infinitamente mais leve que a lista pois somente o primeiro valor esta salvo na lista, o restante tem que ser chamada, por isso sua vantagem é em momoria 
contudo, ele é bem mais lento e tem que chamar um valor por vez com next já que não esta tudo salvo, ele não tem indices sendo obrigando a navegar sequencialmente, 
ou seja, ele é lento mas é mais leve
'''