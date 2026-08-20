from random import randint
computador = randint(0, 10)
print('Sou seu computador... acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')

acertou = False
contador = 0

while acertou == False:
    jogador = int(input('Qual é o seu palpite? '))

    if jogador == computador:
        acertou = True
        contador += 1
    else: 
        if jogador < computador:
            print('Um pouco mais alto')
        else:
            print('Um pouco mais baixo')
            
    contador += 1
    
print('Acertou')
print('Foram necessário {} tentativas' .format(contador))