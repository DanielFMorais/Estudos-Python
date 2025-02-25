'''
Crie um programa que verifica se um número digitado pelo usuário é primo.
'''

valor = input ('Por favor, informe um valor inteiro: ')

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numero = int(input("Digite um número: "))
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")