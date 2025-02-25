#Peça ao usuário para inserir a base e a altura de um triângulo e calcule a sua área

valor_base_triangulo = float(input('Por favor, me informe o valor da base do triângulo: '))
valor_altura_triangulo = float(input('Por favor, me informe a altura do triângulo: '))

formula_area = (valor_base_triangulo * valor_altura_triangulo) / 2

print (f'A área do triângulo = {formula_area}')