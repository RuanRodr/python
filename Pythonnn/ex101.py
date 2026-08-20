from datetime import datetime

def voto(x):
    if datetime.now().year - x < 16:
        return 'Voto negado'
    elif datetime.now().year - x == 16 or datetime.now().year - x == 17:
        return 'Voto opcional'
    else:
        return 'voto obrigatorio'



nasc = int(input('Digite o ano de seu nascimento: '))
data = datetime.now().year - nasc

task = voto(nasc)
print(f'Com {data} anos: {task}')