'''
Faça uma lista de compras com listas 
o usuário deve ter a possibilidade de inserir, aagar e lsitar valores da sua lista
não permita que o programa quebre com erro de indices inexistentes na lista
'''
lista_de_compras = []
import os
while True:
    print ('==' * 20)
    print ('Por favor, selecione uma opção:')
    escolha = input ('[i]ncerir  [a]pagar  [l]istar  [s]air: ')
    
    if escolha == 'i':
        os.system ('cls')
        print ('==' * 20)
        novo_item = input ('Informe o item a adiconar: ')
        if len(novo_item) > 1:
            lista_de_compras.append(novo_item)
            print ('--' *5)
            print (f'{novo_item} adiconado com sucesso!')
        else: 
            print ('Por favor, digite um item para adicionar na lista')
    elif escolha == 'a':
        try:
            os.system ('cls')
            print ('==' * 20)
            valor_remover = input ('Digite o Item que você deseja deletar da lista: ')
            lista_de_compras.pop(int(valor_remover))
            print ('Removido com sucesso!')
        except: 
            print('Escolha o número do item que está na lista')
    elif escolha == 'l':
        os.system ('cls')
        print ('==' * 20)
        for indice_lista, nome in enumerate(lista_de_compras):
            print ('--' *5)
            print (indice_lista, nome)
    elif escolha == 's':
        break
    else:
        print ('Por favor, escolha uma das opções')
        continue
