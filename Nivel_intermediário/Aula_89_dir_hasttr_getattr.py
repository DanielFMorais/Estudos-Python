#dir, hasattr e gatattr em python 

# dir mostra todos os metodos que tal coisa tem no python, por exemplo um str tem metodos para ela como oo uper 

#hasattr basicamente verifica se tem tal metodos e assim vc pode fazer algo sem medo 

# o gatattr basicamente permite verificar se vc definir uma variavel com aquele tal método, ele basicamente permite usar de forma dinamica 

metodo = 'upper'


string = 'Daniel'

if hasattr(string, 'upper'):#é obrigatório colocar entre aspas
    
    print ('Existe upper')
    print (string.upper())
    print (getattr(string, metodo)())
