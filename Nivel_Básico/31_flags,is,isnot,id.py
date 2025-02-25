'''
Flag (Bandeira) - Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
'''
# v1 = 'a'
# v2 = 'a'
# print(id(v1)) 140717035356128
              
# print(id(v2)) 140717035356128
# não produza varivaies dentro de blocos

condicao = True
passou_no_if = None

if condicao:
   passou_no_if = True
   print ('faca algo')
else:
   print ('não faça algo')

if passou_no_if is None:
   print('Não passou no IF')
else: 
   print('Passou no IF')