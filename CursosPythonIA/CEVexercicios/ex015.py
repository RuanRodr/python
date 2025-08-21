dias = int(input('Quantos dias o carro ficou alugado? \n'))

km = float(input('Quantos quilometros foram rodados durante esses dias? \n'))

valordia = dias * 60
valorkm = km * 0.15
valortotal = valordia + valorkm

print('O valor da diaria ficou R${:.2f}, o valor por km ficou R${:.2f} e o valor total R${:.2f}'.format(valordia, valorkm, valortotal))