lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)#tudo que vier antes do for vai ser o que vai ser adicionado
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)