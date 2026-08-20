lista = []
termo = True
valor = 0

while True:
    
    stri = str(input('Deseja adicionar um número? [S/N] ')).strip().upper()
    if stri == 'S':
        valor = (int(input('Digite o valor: ')))

        for i in range(len(lista)):
            if valor == lista[i]:
                print('Valor duplicado')
                termo = False
                break
            else:
                termo = True


        if termo == True:
            lista.append(valor)
        print(lista)
        
    else:
        print(sorted(lista))
        break
        

