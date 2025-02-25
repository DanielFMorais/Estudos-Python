"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf_usuário = '01787467627'

cpf_fatiado_digit1 = cpf_usuário[:9]
contador_regressivo_digt1 = 10
resultado_digt1 = 0

for digitos1_cpf in cpf_fatiado_digit1:
    resultado_digt1 += int(digitos1_cpf) * contador_regressivo_digt1
    contador_regressivo_digt1 -= 1

primeiro_digito = (resultado_digt1 *10) % 11

if primeiro_digito > 9:
    primeiro_digito = 0
else:
    primeiro_digito = primeiro_digito


###

cpf_fatiado_digit2 = cpf_fatiado_digit1 + str(primeiro_digito)
contador_regressivo_digt2 = 11
resultado_digt2 = 0

for digitos2_cpf in cpf_fatiado_digit2:
    resultado_digt2 += int(digitos2_cpf) * contador_regressivo_digt2
    contador_regressivo_digt2 -= 1

segundo_digito = (resultado_digt2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

resultado = cpf_fatiado_digit1 + str(primeiro_digito) + str(segundo_digito)

if resultado == cpf_usuário:
    print (f'Calculo realizado com sucesso, para o cpf {resultado}')
else:
    print ('CPF invalido')