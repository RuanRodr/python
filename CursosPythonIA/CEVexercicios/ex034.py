salario = float(input('Digite seu salario'))

if salario > 1250:
    salaraio = salario + ((salario * 10) / 100)
else:
    salario = salario + ((salario * 15) / 100)
print('O seu aumento foi para R${:.2f}'.format(salario))