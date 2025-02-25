#isinstace - para saber se objeto é de determinado tipo 

'''sempre que você for fazer uma lista, preferencialmente, use somente um tipo , como str, ou int '''

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1,2), {0, 1}, {'Nome' : 'Daniel'}
]

for item in lista: 
    if isinstance(item, set): #o isinstace basicamente puxa o que for daquele tipo em especifico ou filtra aquele tipo, ele basicamente chama aquele tipo, muito útil em listas caoticas 
        print ('Set:')
        print (item, isinstance(item, set))

    elif isinstance(item, str):
        print ('Str:')
        print (item.upper())#aqui eu filtrei, todas as str e coloquei elas em maiuscula

    elif isinstance(item, (int, float)):#quando colocamos pro exemplo, int, float ali, basicamente estou usando uma função OR/ OU
        print ('Numero:')
        print (item, item *2 )

    else: 
        print ('OUTRO')