from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jodador_1': randint(1,6),
        'jodador_2': randint(1,6),
        'jodador_3': randint(1,6),
        'jodador_4': randint(1,6)}

print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 50)

print('== RANKING DOS JOGADORES ==')

for k, v in jogo.items():
    print(f'{k} com {v}')