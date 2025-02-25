#Escreva um programa que peça ao usuário três notas e calcule a média aritmética delas.
#  Depois,
#  informe se o aluno foi aprovado (média ≥ 7), 
# está de recuperação (média entre 5 e 6.9) ou foi reprovado (média < 5).

print ('=' *50)
nota1= float(input('Por favor, me informe a nota da primeira prova: '))
nota2= float(input('Por favor, me informe a nota da segunda prova: '))
nota3= float(input('Por favor, me informe a nota da terceira prova: '))

media= (nota1+nota2+nota3) / 3 

if media >= 7:
    print ('ALUNO APROVADO')
    print ('=' *50)
elif media >= 5 and media < 7:
    print ('ALUNO DE RECUPERAÇÃO')
    print ('=' *50)
else: 
    print ('ALUNO REPROVADO')
    print ('=' *50)

