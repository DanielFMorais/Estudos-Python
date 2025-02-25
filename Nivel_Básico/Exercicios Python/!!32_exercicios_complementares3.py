
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input ('Por favor, me informe o seu primeiro nome: ')

quant_str = (len(primeiro_nome[::]))

nome_curto = quant_str <= 4
nome_normal = quant_str >= 5 and quant_str <= 6
nome_grande =  quant_str > 6

if quant_str >  1:
    if nome_curto:
        print ('Você tem um nome curto')
    elif nome_normal:
        print ('Você tem um nome normal')
    else:
        print ('Você tem um nome muito grande')
else:
    print('Digite pelo menos uma letra')