lista = []
listaPar = []
ListaImpar = []
valor = 0

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        ListaImpar.append(valor)
    
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar == 'S':
        continue
    else:
        print(lista)
        print(listaPar)
        print(ListaImpar)
        break