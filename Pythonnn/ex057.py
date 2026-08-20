sexo = 'M'

while sexo == 'M':
    veri = str(input('Digite o sexo da pessoa: ')).strip().upper()
    if veri == 'M':
        print('Dados invalidos digite novamente')
    if veri == 'F':
        sexo = veri
print('Fim')