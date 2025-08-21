from datetime import date

nasc = input('Digite o ano de nascimento')
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('Mirin')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')