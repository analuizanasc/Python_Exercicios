from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastro'
abrirarquivo(arq)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if opcao == 1:
        cabecalho('Opção 01 - Pessoas cadastradas')
        lerarquivo(arq)
    elif opcao == 2:
        cabecalho('Opção 02 - cadastrar pessoas')
        dic_cadastro = {}
        while True:
            nome = str(input('Nome:'))
            idade = int(input('Idade:'))
            cadastrar(arq, nome, idade)
            continuar = str(input('Continuar? [s/n]')).upper().strip()
            if continuar == 'N':
                break


    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mDigite um opção válida!\033[m')
    sleep(1)
