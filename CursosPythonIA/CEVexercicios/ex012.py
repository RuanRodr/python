produto = float(input('Qual o valor do produto?'))
desconto =  produto - (produto * 5 / 100)
print('O produto de R${} sai por R${}'.format(produto, desconto))