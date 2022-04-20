conta = maior = homens = mulher = 0
while True:
    conta += 1
    print('\033[34m-\033[m' * 20)
    print(f'\033[1:34mCADASTRE UMA PESSOA\033[m')
    print('\033[34m-\033[m' * 20)
    i = int(input(f'Idade:'))
    s = str(input(f'Sexo:[F/M]:')).strip().upper()[0]
    while s not in'FfMm':
        s = str(input(f'Erro! Sexo [F/M]:')).strip().upper()[0]
    if i >= 18:
        maior += 1
    if s in 'mM':
        homens += 1
    if s in 'fF' and i < 20:
        mulher += 1
    print('-' * 30)
    p = ' '
    while p not in 'SN':
        p = str(input('Deseja continuar [S/N]:')).strip().upper()[0]
    if p in 'Nn':
       break
print(f'\n\n{maior} maior(es) de 18 anos.')
print(f'{homens} homen(s) cadastrados.')
print(f'{mulher} mulher(es) com menos de 20 anos cadastrada(s).')





