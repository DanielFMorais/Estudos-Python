# SEP é separador, serve para determinar o que vai separar o que esta na virgula, se não tiver nada, vai ser naturalmente um espaço.
# Comando END define o que acontecerá no final do do codigo, no caso os comandos \r\n servem para pular uma linha no final, de fabrica ele já pula uma linha
# Ele pode definir também se terá a quebra de linha ou não, colocar espaço vazio não vai ter quebra de linha
print(12, 34, sep="-", end="\r\n")
print(56, 78, sep="-", end="\n")
print(299, 132, sep="-", end=" ")
print(56, 78, sep="-", end=" ")