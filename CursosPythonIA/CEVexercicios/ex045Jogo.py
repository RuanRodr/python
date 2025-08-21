from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)

print('Suas Opcões: \n (0) Pedra \n (1) Papel \n (2)Tesoura')
jogador = int(input('Qual a sua jogada?'))

# print('O computador escolheu {}'.format(itens[computador]))

print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))

if jogador == computador:
    print('Empate')
elif jogador == 0 and computador == 1:
    print('Computador ganhou')
elif jogador == 0 and computador == 2:
    print('Jogador ganhou')

elif jogador == 1 and computador == 0:
    print('jogador ganhou')
elif jogador == 1 and computador == 2:
    print('Computador ganhou')

elif jogador == 2 and computador == 0:
    print('Computador ganhou')
elif jogador == 2 and computador == 1:
    print('Jogador ganhou')

else:
    print('Jogada invalida')