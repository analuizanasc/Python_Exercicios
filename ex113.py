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


def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número real válido.\033[m')
            continue #continua no loop- dando erro- até sair
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompido pelo usuário.\033[m')
            return 0
        else:
            return n

#Programa principal
n1 = leiaint('Digite um número inteiro:')
n2 = leiafloat('Digite um número real:')
print(f'Você acabou de digitar o número inteiro {n1} e o número real {n2}.')