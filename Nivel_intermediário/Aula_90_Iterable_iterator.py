#generator expression, iterables e iterators em python

#iteralvel tem obrigação de deter os valores 

#iterator ele te entraga um valor por vez, ou seja um entrega todos os valores enquanto o outro entrega um por vez
#isso faz com que ele não saiba qual é o primeiro ou ultimo,  ele so sabe entregar o proximo valor

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() #tem __iter__ e __next__

'''
iter(iterable) == iterable.__iter__
next(iterable) == iterable.__next__

FAZ A MESMA COISA ENTÃO PARA QUE VC VAI ME COMPLICAR FDP
'''

print (next(iterator))#ele mostra qual o proximo valor
print (next(iterator))

#o next funciona como etapas, você usou ele mostrou o primeiro item,usou de novo mostrou o segundo e assim vai, mas quando chega no final ele para de atribuir as coisas e da bug