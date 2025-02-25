"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input ('Por favor, me informe que horas são, mas sem os minutos: ')

if hora.isdigit():
    int_hora = int(hora)
    bom_dia = int_hora >= 0 and int_hora <= 11
    boa_tarde = int_hora >= 12 and int_hora <= 17
    boa_noite = int_hora >= 18 and int_hora <= 23

    if bom_dia:
        print ('Bom dia')
    elif boa_tarde:
        print ('Boa tarde')
    elif boa_noite: 
        print ('Boa noite')
    else:
        print ('Você não digitou um numero entre 0h e 23h')
else:
    print ('Você não digitou corretamente')