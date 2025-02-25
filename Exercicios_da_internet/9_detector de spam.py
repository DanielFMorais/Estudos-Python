'''
Você está recebendo muitos emails de spam na sua empresa. 
Para bloqueá-los, você deseja criar um script em Python capaz de detectar um email de spam a partir do seu domínio (o nome após o sinal de @).

Crie uma função em Python para implementar essa funcionalidade. 
A função deve exibir uma mensagem de acordo com o e-mail ser spam ou não.
Para o exercício, considere que e-mails enviados do domínio @xyz.com são mensagens de spam.
'''

def detectar_spam(email):
    if email.endswith('@xyz.com'):
        print (f"O email de {email} é spam.")
    else:
        print (f"O email de {email} não é spam.")


detectar_spam('teste@xyz.com')