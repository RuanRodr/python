numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')
digito = 0

while True:

    digito = int(input('digite um numero de 0 a 20 [999 para sair]: '))
    if digito == 999:
        break
    if digito < 0 or digito > 20:
        print('Tente novamente')
    else:
        print(numeros[digito])
