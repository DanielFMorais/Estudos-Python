# if / elif / else
#se / se não se/  se não
"""
estes processos dependem um do outro, o if é o primeior a ser implementado, caso tiver uma segunda auternativa coloque o elif, e para uma terceira coloque o else

o else é executado quando nenhuma das opções anteriores acontecer, por exemplo caso o usuário não escolha nenhuma das duas opções isso faz com que ele passa ser a exessão e funcione 
caso tiver somente o if, ou seja, todos dependem do if, por questões de lógica o else é coringa, ele são nao declara um valor especifico, caso as opções acima não forem requeridas 
ele ativira, mas pode ter 1 ou 2 opções acima, que ele funciona normalmente

o if pode viver sozinho

o elif pode aparecer quantas vezes quiser no código, ou seja, se vc tiver mais de 2 auternativas é ele que virá 

"""
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print ('Você entrou no sistema')
elif entrada == 'sair':
    print ('Você saiu do sistema')
else:
    print('Você não digitou nenhuma das duas opções do sistema')

print ('FORA DOS BLOCOS')
