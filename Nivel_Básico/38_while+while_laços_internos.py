'''
repetições 
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> é quando um código não tem fim

você tem duas formas de quebrar o laço da função while, ou quebrando o laço com comando break ou fazendo que a condição dela exisitr se torne false

o termo CONTINUE faz com que o laço do while seja cortado voltando de volta ao while no inicio, enquanto o break quebra o laço e pula para fora dele, o continue faz com que volte ao inicio do laço
'''

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print (f'{linha=} {coluna=}') 
        coluna += 1

    linha += 1


print ('FIM')