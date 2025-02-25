'''
Neste exercício, você possui duas listas de Python. Cada lista representa os gastos do mês de dois amigos, 
João e Pedro. Cada valor na lista representa o gasto em uma das semanas do mês:

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

Seu objetivo é encontrar quem gastou mais dinheiro ao longo do mês, João ou Pedro.
 Para isso, crie um código em Python que responda a essa pergunta.
'''

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

if total_gastos_joao > total_gastos_pedro:
    print ('Quem gastou mais foi o João')
if total_gastos_joao < total_gastos_pedro: 
    print ('Quem gastou mais foi o Pedro')
else:
    print ('Os dois gastaram a mesma quantidade de dinheiro')