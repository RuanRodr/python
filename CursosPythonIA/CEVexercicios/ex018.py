from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo desejado: \n'))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}, cosseno {:.2f}, tangente {:.2f}' .format(angulo, seno, cos, tan))