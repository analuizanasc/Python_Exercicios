lista = []
while True:
    n = str(input('Nome do produto:'))
    p = float(input('Valor:'))
    lista.append(n)
    lista.append(p)
    tupla = tuple(lista)
    c = str(input('Continuar? [S/N]')).strip().upper()[0]
    while c not in 'SN':
        c = str(input('ERRO! Continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        break
print('='*40)
print(f'{"LISTAGEM DE PREÇOS" :^40}')
print('='*40)
for pos in range(0,len(tupla)):
    if pos % 2 == 0:
         print(f'{tupla[pos]:.<33}', end="")
    else:
        print(f'R${tupla[pos]:<.2f}')

'''print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS" :^40}')
print('=' * 40)
tupla = ('Pão', 2, 'Suco', 4, 'Carne', 5)

for pos in range(0,len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<33}', end="")
    else:
        print(f'R$ {tupla[pos]:>.2f}')'''
