def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número inteiro válido.\033[m')
            continue #continua no loop- dando erro- até sair
        except KeyboardInterrupt:
            print('Entrada de dados interrompido pelo usuário.')
            return 0
        else:
            return n


def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção:\033[m')
    return opc


def tabela(lista_nome, lista_idade):
    cabecalho('Pessoas cadastradas')
    print(lista_nome)
    print(lista_idade)