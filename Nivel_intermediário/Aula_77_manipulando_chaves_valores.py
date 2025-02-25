# Manipulando chaves e valores em dicionários

pessoa = {}

#para criar uma chave caso não tenha nenhuma

pessoa['nome'] = 'Daniel' #estou criand

print (pessoa['nome'])#a chave precisa existir \\\ estou chamando 

pessoa['Sobrenome'] = 'Fernandes'
pessoa['nome'] = 'Gabriel' #estou modificando o valor

del pessoa['Sobrenome'] #estou excluindo uma chave

print (pessoa)

if pessoa.get('Sobrenome') is None:
    print ('Não existe')
else:
    print (pessoa['Sobrenome'])