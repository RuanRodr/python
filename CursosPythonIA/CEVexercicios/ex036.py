valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
qtdAnos = int(input("Em quantos anos deseja pagar? "))

presta = valorCasa / (12 * qtdAnos)

lim = salario * 0.3

if presta > lim:
    print("Emprestimo negado")
else:
    print("Emprestimo confirmado")