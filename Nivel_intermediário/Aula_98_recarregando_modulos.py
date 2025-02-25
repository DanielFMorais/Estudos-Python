# import aula_98_m

# print (aula_98_m.variavel)

# '''Modulos importados so tem um valor por importação, então se vc ficar mandando repetir varias vezes ele não vai'''

# for i in range (10):
#     import aula_98_m
#     print (i)

# print ('Fim')

'''Para isso imortamos uma biblioteca chamada importlib, que vai recarregar este modulo quantas vezes eu quiser'''
import importlib

import aula_98_m

print (aula_98_m.variavel)

for i in range (10): 
    importlib.reload(aula_98_m)
    print (i)

print ('Fim')