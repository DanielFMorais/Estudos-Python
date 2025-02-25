'''
Solicite ao usuário um número inteiro positivo . Em seguida, calcule e mostre a soma de todos os números pares de 1 até 
'''

valor =int (input('Por favor, me informe um valor inteiro positiovo: '))

lista_valor = []
lista_valor_par = []
for i in range(0, valor + 1):
    lista_valor.append(i)
    
for i in lista_valor:
    if i % 2 == 0:
        lista_valor_par.append(i)

print (f'Os digitos escolhidos foram: {lista_valor}')
print (f'Os valores pares do selecionado são: {lista_valor_par} e a soma deles = {sum(lista_valor_par)} ')


#podia ser resolvido assim 

'''
n = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(2, n + 1, 2):
    soma += i

print(f"A soma dos números pares de 1 a {n} é: {soma}")

'''