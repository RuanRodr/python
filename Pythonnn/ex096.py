def area(x, y):
    total = x * y
    print(f'A área do terreno {x}x{y} é de {total} m²')
    return total


largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o  comprimento do terreno: '))

area(largura, comprimento)
