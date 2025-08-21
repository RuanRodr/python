km = int(input('Digite quantos km vc vai pra puta que pariu'))
total = 0.0
if km <= 200:
    total = km * 0.50
    print('O valor da passagem com tarifa de R$0,50 é R$ {:.2f}' .format(total))
else:
    total = km * 0.45
    print('O valor da passagem com tarifa de R$0,45 é R$ {:.2f}' .format(total))