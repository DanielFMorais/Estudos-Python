# cpf_usuário = '746.824.890-70'.replace('.', '').replace('-', '').replace(' ', '')# O REPLACE MODIFICA O CARACTERE QUE VC QUER POR OUTRO QUE VC ESCOLHER, 
# #PERMITINDO RECEBER ATE MESMOTE TEXTOS QUE NÃO QUERIA
'''
cpf_usuário = re.sub(r'[^0-9], '', '746.824.890-70') faz a mesma coisa so que so considera numeros então vc pode escrever qualqeur merda ali, permitindo ter confiança para pedir para o usuário
o cpf dele
'''
import re 
import sys

entrada = input ('Digite o CPF: ')

cpf_usuário = re.sub(r'[^0-9]', '', entrada)

entrada_sequencial = entrada == entrada [0] * len(entrada)

if entrada_sequencial:
    print ('Vocé digitou valores sequenciais')
    sys. exit()


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
    print (f'o CPF {resultado} é válido!')
else:
    print ('CPF invalido')

