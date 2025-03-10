"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
# CPF == 661.009.820-48

cpf = '74682489070'

cpf_fatiado = cpf[:9]
contador_regressivo_digt1 = 10
resultado_digt1 = 0

for digitos1_cpf in cpf_fatiado:
    resultado_digt1 += int(digitos1_cpf) * contador_regressivo_digt1
    contador_regressivo_digt1 -= 1

primeiro_digito = (resultado_digt1 *10) % 11

if primeiro_digito > 9:
    primeiro_digito = 0
else:
    primeiro_digito = primeiro_digito

#isso daqui também poderia ser  => primeiro digito = primeiro digito if primeiro digito <= 9 else 0

                 