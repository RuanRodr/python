produto = float(input('Digite o valor do produto'))

escolha = int(input('Faça a escolha de pagamento: \n (1) A vista \n (2)A vista no cartão \n (3) 2x Cartao \n (4) 3x cartao'))

if escolha == 1:
    desconto = produto * 0.10
    produto = produto  - desconto
    print('O valor do produto ficou em R${} com 10% de desconto' .format(produto))

elif escolha == 2:
    desconto = produto * 0.05
    produto = produto  - desconto
    print('O valor do produto ficou em R${} com 5% de desconto' .format(produto)) 

elif escolha == 3:
    produto = produto / 2
    print('O valor do produto ficou em R${} em 2x' .format(produto)) 

elif escolha == 4:
    juros = produto + (produto * 20 / 100)
    totalparcelas = int(input('Quantas parcelas?'))
    parcela = juros / totalparcelas
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparcelas, parcela))
    print('O valor do produto ficou em R${}' .format(juros)) 
else:
    print('Opcao invalida')