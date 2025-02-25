# exemplo de uso dos sets

letras = set()

while True:
    letra = input ('Digite uma letra: ')
    letras.add(letra.lower())

    #quero que a letra que ele ache seja a letra L

    if 'l' in letras:
        print ('Parabens você encontrou a letra misteriosa')
        break

    print (letras)