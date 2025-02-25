"""
CONTANTE = "variáveis" que não vão mudar
Muitas condições no mesmo if (ruim) / OU SEJA, QUANTO MAIS AND, NOT, OR  NO SEU IF MAIS DIFICIL E COMPLEXO É O CÓDIGO E ENTENDER SE VAI OU NÃO ENTRAR
    <- contagem de complexidade (ruim) / OU SEJA, MUITOS TABS OU QUANTO MAIS LONGE O SEU CÓDIGO ESTIVER DO CANTO, MAIS COMPLEXO E COMPLEXIDADE NA PROGRAMAÇÃO NUNCA É FAVORÁVEL

USAMOS LETRAS MAIUSCULAS PARA COISAS QUE NÃO VÃO MUDAR NO CÓDIGO
"""

velocidade = 61 # velicidade atual do carro
local_carro = 101 # local em que o carro esta na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # A distânica onde o radar pega

acima_da_velocidade = velocidade > RADAR_1
CARRO_ESTA_NO_RADAR = local_carro <= (LOCAL_1 + RADAR_RANGE) and local_carro >= (LOCAL_1 - RADAR_RANGE)


# if velocidade > RADAR_1:
#     print ('O carro está acima da velocidade permitida')
# else:
#     print ('O carro esta na velocidade permitida')                                                                    CODIGO SUJO

# if (velocidade > RADAR_1) and (local_carro <= (LOCAL_1 + RADAR_RANGE) and local_carro >= (LOCAL_1 - RADAR_RANGE)):
#     print ('MULTA GERADA')

#codigo limpo abaixo

if acima_da_velocidade:
    print ('O carro está acima da velocidade permitida')
else:
    print ('O carro esta na velocidade permitida')

if CARRO_ESTA_NO_RADAR:
    print ('O carro passou pelo radar')

if acima_da_velocidade and CARRO_ESTA_NO_RADAR:
    print ('MULTA GERADA')

