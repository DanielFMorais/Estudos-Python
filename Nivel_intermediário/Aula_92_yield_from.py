## Yield from
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')

# def gen2():
#     print('COMECOU GEN2')
#     yield from gen1 #puxa os valores do yield antigo que vc selecionar
#     yield 4
#     yield 5
#     yield 6
#     print('ACABOU GEN2')

def gen2(gen=None):
    if gen is not None: #vc pode colocar ifs nestas funções
        yield from gen #o yield from puxa os valores do yield antigo
    print('COMECOU GEN2')
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()