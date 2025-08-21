velo = float(input('Velocidade: '))

if velo >= 80:
    acrescimo = (velo - 80) * 7
    if acrescimo != 0:
        print('Você recebeu uma multa de R${}' .format(acrescimo))   
    else: 
        print('Vc foi multado')
else:
    print('Nos te pega arrombado')