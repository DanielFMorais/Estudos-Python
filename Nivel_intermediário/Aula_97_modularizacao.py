# Modularização - Entendendo os seus próprios módulos Python
'''
é quando vc basicamente usa outras pastas no programa, seria a mesma coisa de eu usar o que esta na aula 20 aqui nestea aula 97, entende?
isso é feito o tempo todo, por isso tem que entender bem
'''

# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
'''
Mas cuidado, vc deve tomar cuidado para não importar nome de módulos com nomes iguais a outros módulos pre definidos pelo python como o sys por exemplo 
'''

# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

'''
Ele reconhece pastas dentro da parta que ele mesmo esta, e de pastas que estão nas pastas que ele ta, mas nunca uma pasta fora da que ele esta
'''
'''
Isso basicamente que vc pode chamar facilmente qualquer módulo que esta na mesma parta, no caso aqui, tudo que esta no nivel intermédiário seria 
facilmente chamado, mas caso eu quisesse algo que esta no nivél básico seria diferente
Por isso também que foi dito que os nomes das pastas não pode ter espaços nem caracteres especiais, pois eles são considerados módulos e podem alguma hora serem chamados
'''
# import sys

# import aula_97_modulo

# print('Este módulo se chama', __name__)
# print (sys.path, sep= '\n')

"""
Podemos utilizar tudo o que esta no modulo antigo, funciona da mesma forma que usar um modulo do sys por exemplo, usamos o nome do modulo depois um ponto e a variável


"""

import aula_97_modulo
from aula_97_modulo import varivavel_modulo, soma

print(aula_97_modulo.varivavel_modulo)

print (soma(2, 2))
print (aula_97_modulo.soma(2,2))#os dois faz a mesma coisa, um somente é menor que o outro 