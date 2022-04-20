from time import sleep
from ex115.lib.interface import cabecalho


def abrirarquivo(nome):
    try:
        a= open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        a = open(nome, 'wt+')
        sleep(.5)
        print('Criando arquivo...')
    else:
        print('Arquivo encontrado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Problema ao ler arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado[1]:>3}')
    finally:
        a.close()

def cadastrar(arq, nome= 'desconhecido', idade=0):
    try:
        a = open(arq, 'at') # a de append (adicionar)
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade} anos')
        except:
            print('Houve um erro na hora de escreves os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

