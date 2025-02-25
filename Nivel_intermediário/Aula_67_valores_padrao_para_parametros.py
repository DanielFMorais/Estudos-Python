"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

#usado para quando vc tem um valor que vc não saberá se sera usado ou n
def soma(x, y, z=None): #aqui basicamente defini ele como um não valor para assim poder tratar valores bool. já que se eu usasse o zero, eu basicamente iria falar que ele é falso
    if z is not None: #para saber se o z foi enviado ou n
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)