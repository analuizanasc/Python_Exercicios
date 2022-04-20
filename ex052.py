n = int(input('Digite um número inteiro:'))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        #print('\033[34m', end=' ')
        tot += 1
    #else:
        #print('\033[m', end=' ')
    #print(f'{c}', end='')
#print(f'\n\033[m{n} é divisível {tot} vezes.')
if tot == 2:
    print('Ele é um número primo!')
else:
    print('Ele não é um número primo!')



#não consegui