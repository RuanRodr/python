countHomens = 0
countIdade = 0
CountMulheresVinte = 0


while True:
 
    print('-'*20)
    print('Cadastre uma pessoa')
    print('-'*20)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()

    if idade > 18:
        countIdade += 1
    if sexo == 'M':
        countHomens += 1
    if sexo == 'F' and idade < 20:
        CountMulheresVinte += 1

    continuar = str(input('Quer continuar? [S/N] '))
    if continuar == 'N':
        break

print(f'Pessoas com mais de 18 anos -> {countIdade}')
print(f'Homens cadastrados -> {countHomens}')
print(f'Mulheres com menos de 20 anos {CountMulheresVinte}')
