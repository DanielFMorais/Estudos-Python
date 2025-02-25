"""
Conversão de tipos, coerção, type convertion, typecasting, Coercion
 é o ato de converter um tipo em outro tipo imutáveis e primitivos: str, int, float, bool
"""
print ("1", type("1"))
print (int("1"), type(int("1")))

#se eu quisesse fazer uma soma de 1 + 1, se estivesse escrito 
#print('1' + 1 ) => erro 

print(int('1') + 1) # desta forma seria realizada a equação corretamente, pois os dois são considerados int depois da conversão

# o Python entende perfeitamente calculos realizados com float e com int, no entento se for realiado calculos assim, o valor final será float

print(float('2') + 2 ) # resultado = 4.0 
print(type (float('2') + 2 )) # lembrando que os parenteses são lidos de dentro para fora e o resultado vai ser o ultimo valor
print(bool(' '))

#da para fazer essa conversões com qualquer tipo

print(str(11) + 'B') #Lembrando que para converter tem que fazer sentido, logicamente um tipo str que não seja um numero não pode ser convertido para um int
# a letra B não seria um INT