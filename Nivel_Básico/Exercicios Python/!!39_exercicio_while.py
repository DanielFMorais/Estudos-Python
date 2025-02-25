nome = input ('Por favor, me diga qual é o seu nome:')

tamanho_nome = len(nome)
print (f'Seu nome tem exatamente {tamanho_nome} caracteres')

contador = 0
novo_nome = ''
while contador < tamanho_nome:
    letra = nome[contador]
    novo_nome += '*' + letra + '*'
    contador += 1

print (novo_nome)