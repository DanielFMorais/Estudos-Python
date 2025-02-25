#try, except, else, finally

'''
try e else não funcionam sozinhos
'''
'''
Não devemos usar o try e except juntos, por mais que ele funcione ele esconde um erro, já que ele basicamente irá ignorar qualquer errro e vai dar continuidade ao código,
mas isto é ruim,devido que, vc deve saber todos os erros que seu código dá, vc deve sempre tratar o erro sabendo qual erro deu, sem silencialos
'''

# try:
#     a = 10
#     print ('linha 1')
#     b = 0 
#     c = 10 / 0
#     print ('linha 2')
# except:
#     print('Estou escondendo o erro')
#     '''NUNCA FAÇA ESSAS COISAS CARA, VC NÃO TEM MEMORIA PARA SABER OS ERROS QUE COMETE NÃO'''

#o try tenta fazer o programa e para quando o erro acontece, ou seja, ele exibiria somente a linha 1 ali encima

'''
COMO USAR O EXCEPT CORRETAMENTEO
para usar ele corretamente, você deve informar qual erro
'''

try:
    a = 10
    b = 0 
    print ('linha 1')
    c = 10 / 0
    print ('linha 2')
except ZeroDivisionError:
    print('Estou dividindo por zero')
#agora se vc cometer qualquer erro que não zero o divizivel por zero, vc seria informado, por exemplo, se vc não declarar uma variável, vc vai saber
#para tratar mais de uma excessão basta colocar mais de 1 except
except NameError:
    print ('Você esqueceu uma variável')
except Exception:
    print ('Esta é a maior classe de erro, geralmente usamos para falar de um erro desconhecido, pois ele trata qualquer erro que não esteja trantando')
#except (TypeError, IndexError) se vc colocar entre parenteses formando uma tuple,vc pode tratar varios erros em um unico except 

'''
Para sabermos qual erro apareceu e mostrar na tela que ele ocorreu podemos fazer o seguinte
'''
try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error: #usamos o as... assim informamos que a variável que criamos error, vai receber aqueles dois ali
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)# e para vc mostrar qual erro é podemos usar essa estrutura, a __class_ para informar a classe e a __name__ para falar o nome daquela classe
    #aqui vc basicamente fala qual classe foi ativada, e com base nisso essas estruturas complicadas funcionam
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')

#classe é o objeto em si, e instancia é oq está atribuido aquele objeto 