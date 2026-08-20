dados = dict()
partidadasLista = list()
gols = 0
somaGols = 0

dados['jogador'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))

for i in range(partidas):
    gols = int(input(f'Quantos gols na partida {i}?'))
    partidadasLista.append(gols)
    somaGols += gols

dados['gols'] = partidadasLista
dados['total'] = somaGols

print('-=' * 40)
print(dados)
print('-=' * 40)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)

print(f'O jogador {dados['jogador']} jogou {partidas}')
for i in range(partidas):
    print(f'=> Na partida {i}, fez {partidadasLista[i]} gols')
print(f'O total de gols foi {somaGols}')