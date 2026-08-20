n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
resultado = 0
while opcao != 5:
    print('''        [1] somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do Programa''')
    opcao = int(input(('Qual é a sua opção? ')))

    if opcao == 1:
        resultado = n1 + n2
        print(resultado)

    elif opcao == 2:
        resultado = n1 * n2
        print(resultado)

    elif opcao == 3:
        if n1 > n2:
            resultado = n1
            print('n1 é maior')
        else:
            print('n2 é maior')
    elif opcao == 4:
        print('Escreva os numeros novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opcao invalida')
print('Fim do programa')