lista = []
count = 0

valor = int(input('Digite um valor: '))
lista.append(valor)

while True:

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()

    if continuar == 'S':
        valor = int(input('Digite um valor: '))
        lista.append(valor)
        print(lista)
        count += 1
    else:
        if 5 in lista:
            print('O valor 5 está na lista')
        else:
            print('O valor 5 nao esta na lista')
        lista.sort(reverse=True)
        print(lista)
        break
    
    