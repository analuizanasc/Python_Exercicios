'''print('-' * 20)
print('BANCO ANA')
print('-' * 20)
while True:
    valor = int(input('Quanto você quer sacar? R$ '))
    nota50 = valor % 50
    if nota50 == 0:
        qtd50 = valor / 50 # quantas notas de 50
        print(f'nota(s) de 50: {qtd50}')
    else:
        qtd50 = valor // 50 #quantas notas de 50  ( sem resto )
        resto50 = valor % 50  # resto da divisão com 50 -> Quanto sobra após retirar as notas de 50
        if qtd50 != 0:
            print(f'{qtd50} nota(s) de R$50,00')
        if resto50 % 20 == 0: #quanto sobrou > tem nota de 20?
            qtd20 = resto50 / 20
            print(f'{qtd20} nota(s) de R$20,00')
        else:
            qtd20 = resto50 // 20
            resto20 = resto50 % 20
            if qtd20 != 0:
                print(f'{qtd20} nota(s) de R$20,00')
            if resto20 % 10 == 0:
                qtd10 = resto20 / 10
                print(f'{qtd10} nota(s) de R$20,00')
            elif resto20 % 10 != 0:
                qtd10 = resto20 // 10
                resto10 = resto20 % 10
                if qtd10 != 0:
                    print(f'{qtd10} nota(s) de R$10,00')
                if resto10 % 1 == 0:
                    qtd1 = resto10 // 1
                    print(f'{qtd1} nota(s) de R$1,00' )
    continuar = str(input('Deseja sacar outro vaor? [S/N]')).strip().upper()[0]
    while continuar not in 'SnNn':
        continuar = str(input('erro! Deseja sacar outro vaor? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break'''

valor = int(input('Quanto você quer sacar? R$ '))
total = valor
céd = 50
qtd = 0
while True:
    if total >= céd:
        total -= céd
        qtd += 1
    else:
        if qtd > 0:
            print(f'Total de {qtd} cédulas de R$ {céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        qtd = 0
        if total == 0:
            break



