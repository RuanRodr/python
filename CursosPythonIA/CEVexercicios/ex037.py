num = int(input("Digite um número inteiro: "))
escolha = int(input("faça uma escolha \n (1)binario (2)octal (3)hexadecimal )"))

if escolha == 1:
    print(bin(num))
elif escolha == 2:
    print(oct(num))
elif escolha == 3:
    print(hex(num))
else:
    print("Escolha de forma correta")