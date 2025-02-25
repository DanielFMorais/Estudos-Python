# 1. (n + n) # parenteses são executados de dentro para fora
# 2. **
# 3. *  /   //   %
# 4. +   - 

#Se tiver a mesma precedencia, então vai ser executado da esquerda para a direita

#isso é basicamente a ordem que as contas são feitas, obviamente é so seguir o que vc aprendeu no basico da escola sobre equações

conta_1 = 1 + 1 ** 5 + 5 # 7
conta_1a = (1 + 1) ** (5 + 5) # 1024
Conta_1b = (1 + int(0.5 + 0.5)) ** (5 + 5) #1024

#adendo: como o código ele entende de cima para baixo, se eu tiver uma variável com o mesmo nome, a que estiver mais embaixo que vai ser utilizada no codigo final 
print(conta_1)
print(conta_1a)
print(Conta_1b)