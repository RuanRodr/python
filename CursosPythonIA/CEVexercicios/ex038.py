num1 = int(input("Digite o primeiro numero inteiro"))
num2 = int(input("Digite o segundo numero inteiro"))

if num1 > num2:
    print("{} é maior que {}".format(num1, num2))
elif num2 > num1:
    print("{} é maior que {}".format(num2, num1))
else:
    print("Os dois numeros sao de mesmo valor")