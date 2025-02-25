
'''
Iteráveis -> str, range, etc SÃO VALORES QUE TE ENTRAGAM UM VALOR POR VEZ
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor 
iter -> me entre seu iterador

metodo => uma ação que vc vai chamar dentro do seu objeto  
'''

# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
