lista = []
while True:
    num = int(input('Digite um número:'))
    print('Adicionado com sucesso!')
    lista.append(num)
    lista = list(set(lista))
    lista.sort()
    cont = str(input('Deseja continuar? [S/N]')).upper()[0]
    while cont not in 'SN':
        cont = str(input('ERRO! Deseja continuar? [S/N]')).upper()[0]
    if cont == 'N':
        break
print(f'Você digitou os números: {lista}')
