resp = 'S'
divisor = 0
media = 0
menor = 0
maior = 0

while resp in 'Ss':
    
    num = int(input('Digite um número'))
    media += num
    divisor += 1

    if divisor == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

resultado = media / divisor

print('A media dos numeros é {}' .format(resultado))
print('O maior e o menor numeros são {} e {} respectivamente' .format(maior, menor))
