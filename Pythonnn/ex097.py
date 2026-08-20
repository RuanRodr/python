def escreva(palavra):
    i = len(palavra)+2
    print('-' * i)
    print(f' {palavra}')
    print('-' * i)


count = str(input('Digite uma palavra: '))

escreva(count)