palavras = ["python", "asimov", "código", "web", "programação"]
# Crie um código que seja capaz de encontrar e exibir a maior e a menor palavra da lista (em número de caracteres).


menor_qtd_carac = palavras[0]
maior_qtd_carac = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_qtd_carac):
        maior_qtd_carac = palavra

    if len(palavra) < len(menor_qtd_carac):
        menor_qtd_carac = palavra

print (f'A maior palavra é {maior_qtd_carac}')
print (F'A menor palavra é {menor_qtd_carac}')
