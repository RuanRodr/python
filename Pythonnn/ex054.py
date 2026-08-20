from datetime import date

anoAtual = date.today().year
totalmaior = 0
totalmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? ' .format(pess)))
    idade = anoAtual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade' .format(totalmaior))
print('Ao todo tivemos {} pessoas menor de idade' .format(totalmenor))
