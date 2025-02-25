'''
Fatiamento de strings
 012345678
 olá mundo
-987654321
Fatiamento [i:f:p] [::] (i = inico / f = fim / p = passo)
obs.: a função len retorna a qtd de caracteres da str
'''
variavel = 'Olá mundo'

print (variavel[5])
print (variavel[4:])#ai aqui vai ate o final da string
print (variavel[4:8]) #ai você definiu um inicio que é na casa 4 e o final na casa 8, mas lembrando que o python vai ocultar a ultima casa, então so vai mostrar ate o mund
print (variavel[0:5])
print (variavel[:5])#se voce omite o inicio, ele entende que é para começar do inicio 
print (len(variavel[:5]))#espaço também é caractere
print (len(variavel))
print (variavel[0:len(variavel):1])# o final é o passo, que diz de quantas em quantos caracteres ele vai pular
print (variavel[0:len(variavel):2])
print (variavel[::-1]) #colocar valores negativos ele basicamente vai contar invertido (obviamente) muitas das vezes escree de tras para frente
