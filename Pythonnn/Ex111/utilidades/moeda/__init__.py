from multiprocessing import resource_sharer
from pickle import TRUE

'''
Calcula o aumento de um determinado preço,
retornando o resultado com ou sem formatação.
:param preço: o preço que se quer reajustar
:param taxa: qual é a porcentagem do aumento
:param formato:quer a saida formatada ou não?
:return: o valor reajustado, com ou sem formato.
'''
def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco = 0, formato = False):
    res = preco / 2
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco = 0, taxa = 10, taxar = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'Com {taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
    print('-' * 30)