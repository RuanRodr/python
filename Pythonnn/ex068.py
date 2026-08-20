from random import randint
count = 0

while True:
    jogador = int(input('Digite um valor de 1 a 10: '))
    escolha = str(input('Par ou impar? [P/I]: ')).strip().upper()
    computador = randint(1, 10)
    soma = jogador + computador
    

    print(f'Você jogou {jogador} e o computador {computador}, total {soma}')

    if soma % 2 == 0 and escolha == 'P':
        print('Deu par')
        print('Você venceu')
        count += 1

    if soma % 2 == 0 and escolha == 'I':
        print('Deu par')
        print('Você perdeu')
        break

    if soma % 2 != 0 and escolha == 'P':
        print('Deu impar')
        print('Você perdeu')
        break

    if soma % 2 != 0 and escolha == 'I':
        print('Deu impar')
        print('Você venceu')
        count += 1

print(f'Voce venceu {count} vezes')

