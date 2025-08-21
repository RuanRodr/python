from datetime import date

nasc = int(input('Digite seu ano de nascimento'))
atual = date.today().year
idade = atual - nasc

if idade == 18:
    print('Voce tem que se alistar nesse ano')
elif idade < 18:
    print('Voce ainda n tem idade para se alistar, faltam {} anos'.format(18 - idade))
else:
    print('Voce ja deveria ter se alistado há {} anos'.format(idade - 18))