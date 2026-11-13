from python.Pythonnn.Ex115.lib.interface import *
from python.Pythonnn.Ex115.lib.arquivo import *
import time

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas',  'Sair do Sistema'])
    if resposta == 1:
        #opcao de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        #opcao de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print('Erro! Digite uma opção valida')
    time.sleep(2)
