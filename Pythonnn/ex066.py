num = 0
soma = 0
count = 0

while num != 999:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    count += 1
    
print(f'A soma dos {count} valores foi {soma}')