"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2

print (numero3)
print (f'{numero3:.2f}') #aqui vc retorna str
# aqui vc soluiciona esse imprecisão formatando

print(round(numero3, 2)) #aqui vc retorna como numero flutuante mesmo, a função round serva para isso, falar quantas casas depois da virgula queremos
#mas se tiver zeros depois do final da virgula ele vai simplesmente ignorar elas

'''
a outra forma de resolver isso é usando um modulo de decimal imporatdo, que é util para coisas com mitas casas decimais ou que precisam de muita precisão 
'''

import decimal 

numero1 = decimal.Decimal('0.1')
numero2 = decimal.Decimal('0.7')
numero3 = numero1 + numero2
print (numero3)
#MAIS PRECISA