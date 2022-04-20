lista = []
while True:
    num = int(input('Digite um número:'))
    lista.append(num)
    lista.sort(reverse=True)
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('ERRO! Deseja continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break

print('-'*30)
print(f'{"RELATÓRIO":^30}')
print('-'*30)
print(f'Foram digitados {len(lista)} números.')
print(f'A lista em forma decrescente é: {lista}')
if 5 in lista:
    print('O 5 está na lista')
else:
    print('O 5 não tá na lista')
