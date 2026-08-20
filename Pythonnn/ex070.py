total = 0
countMil = 0
barato = 0
nomeBarato = ''

produto = str(input('Nome do produto: '))
preco = float(input('Preço: R$'))

nomeBarato = produto
barato = preco

while True: 
    
    total += preco

    if preco > 1000:
        countMil += 1
    
    if preco < barato:
        nomeBarato = produto        
        barato = preco

    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break

    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))


print('Fim do programa \n\n')

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {countMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R${barato:.2f}')