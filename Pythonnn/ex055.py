menor = 0
maior = 0

for pessoa in range(1, 6):
    peso = float(input('Digite o peso da pessoa {}: ' .format(pessoa)))

    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Peso Maior: \n{}KG \nPeso Menor: \n{}KG' .format(maior, menor))