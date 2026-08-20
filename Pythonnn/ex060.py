num = int(input('Digite o número que será fatorado: '))
fato = num
calculo = 1

while fato != 0:
    calculo *= fato
    print('{} x {} = {}' .format(num, fato, calculo))
    fato -= 1

" cagado "