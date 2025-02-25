gastos_joao = [300, 500, 200, 800]
gastos_pedro = [1000, 400, 500, 700]

# Seu objetivo é encontrar quem gastou mais dinheiro ao longo do mês, João ou Pedro. Para isso, crie um código em Python que responda a essa pergunta.

soma_joao = 0
soma_pedro = 0

for soma in gastos_joao:
    soma_joao += soma

for soma2 in gastos_pedro:
    soma_pedro += soma2

'''
podia ter feito assim também:
total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

já que sum soma todos os valores da lista

'''

if soma_joao > soma_pedro:
    print ('João gastou mais que Pedro.')
elif soma_joao < soma_pedro:
    print ('Pedro gastou mais que João')
else:
    print ('João e Pedro, gastaram a mesma quantidade.')
