import random

random = random.randint(0, 5)

user = int(input('Digite um numero de 0 a 5'))

if random == user:
    print('Parabens vc acertou')
else: 
    print('Burro')
    print('O numero era {}'.format(random))