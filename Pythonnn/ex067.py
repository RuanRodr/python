count = 1
while True:

    num = int(input('Qual numero sera desejado para a tabuada?: '))

    if num < 0:
        break

    while count != 11:
        multi = num * count
        print(f'{num} * {count} = {multi}')
        count += 1
print('Programa encerrado')

