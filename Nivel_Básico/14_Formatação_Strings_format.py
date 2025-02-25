a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={:.2f}'.format(a,b,c) #esta é uma forma de ser feito, vc esta indo por ordem, basicamente 

'''
aqui temos uma aula: vamos lá, basicamente quando vc esta fazendo desta forma, o a esta pucando o primeiro valor, o b o segundo e o c o terceior, mas lembrasse
que tudo começa com 0, então a primeira posição é sempre zero, e dentro daquelas chaves vc pode colocar de qual posição é, se esta na posição 0 ou 2 neste exemplo
'''
formato = 'a={0} b={1} c={2:.2f}'.format(a,b,c)

'''
format também pode ser colocado nomes neles, se tornando parametros nomeados, que é quando vc nomeia o parametros que estão dentro do format
lembrando que se vc começar a nomear 1, vai ter que nomear todos

EM RESUMO, SE VC NÃO NOMEAR NADA E NÃO COLOCAR NADA NOS {}, ENTÃO VAI IR POR ORDEM DA ESQUERDA PARA A DIREITA, SE VC COLOCAR VALORES DENTRO DO {} JA VAI PUXAR O ESPECIFICO E SE VC 
NOMEAR ALGO VAI TER QUE NOMEAR TUDO, ai no caso quando vc for chamar a parametros vc vai chamar pelo nome dele
'''
formato = 'a={nome1} b={nome2} c={nome3:.2f}'.format(nome1=a, nome2= b, nome3= c)
print (formato)
