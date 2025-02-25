"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

print ('-'*50)
nome = input ('Por favor, digite o seu nome: ')
idade = input ('Por favor, digite a sua idade: ')
print ('-'*50)

if idade and nome:
    print ('-'*50)
    print (f'Seu nome é {nome}')
    print ()
    print (f'Seu nome invertido é {nome[::-1]}')
    print ()

    if ' ' in nome:
        print ('O seu nome CONTEM espaços!')
        print ()
    else:
        print ('O seu nome NÃO CONTEM espaços!')
        print ()
    
    print (f'Seu {nome} tem {len(nome)} letras')
    print ()
    print (f'A primeira letra do seu nome é: {nome[0]}')
    print ()
    print (f'A ultima letra do seu nome é: {nome[-1]}')
    print ('-'*50)
else:
    print ('-'*50)
    print ('Desculpe, você deixou campos vazios.')
    print ('-'*50)