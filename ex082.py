lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um número:'))
    lista.append(num)
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('ERRO!Deseja continuar? [S/N]'))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    if cont == 'N':
        break

print(f'O números digitados foram: {lista}')
print(f'Os pares são: {lista_par}')
print(f'Os números ímpares são: {lista_impar}')

