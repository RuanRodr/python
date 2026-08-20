lanche = ('Hambuerguer', 'Suco', 'Pizza', 'Pudim')
#tupla 
print(lanche[1])
print(lanche[1:3])
print(lanche[:2])
print(lanche[1:])

#tamanho de lanche (len)
#for cont in range(0, len(lanche)):

for comida in lanche:
    print(f'eu vou comer {comida}')


a = (2, 5, 4)
b = (5, 8, 1, 2)

c = b + a
print(c.count(5))