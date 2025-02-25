# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html

# Importar o módulo inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# é uma boa pratica
import sys #vc deve colocar o nome inteiro do módulo

print (sys.platform)
# sys.exit () #sai do programa
# print (123)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# partes de módulos - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
from sys import exit, platform
#aqui eu immporte a função exit e a função platform do módulo sys, tipo não faz seu programa ser mais rapido mas fica menor quando vc vai chamar o módulo
# DICA: NOME DE VARIÁVEIS NÃO DEVEM SER IGUAIS A NOMES DE MÓDULOS
print ('123')
exit()#é so escrever como se fosse uma função (no caso é uma função ne,,, mas isso é mais para frente)
print (platform)
#tem a desvatagem também, de não ter a proteção do módulo, então se em algum momento vc sem querer declarar uma variável com esse nome, parabens vc invalidou ele

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# alias 1 - import nome_modulo as apelido '''aqui vc basicamente dá um apelido para o módulo, liberando o nome dele para variáveis'''
import sys as apelido_de_sys #vc importar normalmente, mas coloca o as e o apelido que vc quer

# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex #aqui vc basicamente, modificou o nome da parte do seu módulo 
from sys import platform as pf

print (pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

#AGORA ME FALA SE VC SABE QUE ISSO AQUI É RUIM PARA QUE VC VAI USAR O JAMANTA, MODIFICA O NOME DA SUA VARIÁVEL E NÃO O NOME DO SEU MÓDULO O INTELIGENCIA
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# má prática - from nome_modulo import * #usa isso aqui n 
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
