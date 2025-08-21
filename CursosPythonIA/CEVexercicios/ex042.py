r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar triangulo')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isosceles')
    else:
        print('Escaleno')
else: 
    print('Não forma triangulo')