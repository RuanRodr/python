def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n

num = leiaint('Digite um valor inteiro: ')
print('O valor digitado foi {}' .format(num))