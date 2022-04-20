lista_geral = []
lista_nome = []
lista_notas = []
while True:
    nome = str(input('Digite o nome:'))
    lista_nome.append(nome)
    nota1 = float(input('Digite nota 01:'))
    nota2 = float(input('Digite nota 02:'))
    lista_notas.append(nota1)
    lista_notas.append(nota2)
    lista_nome.append(lista_notas[:])
    lista_geral.append(lista_nome[:])
    lista_nome.clear()
    lista_notas.clear()
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while cont not in 'SN':
        cont= str(input('ERRO! Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == cont:
        break
print('='*40)
print(f'{"No." :<8}', end=' ')
print(f'{ "NOME" :<15}', end=' ')
print(f'{"MÉDIA" :<7}')
print('='*40)
for c in range(0,len(lista_geral)):
    soma = lista_geral[c][1][0] + lista_geral[c][1][1]
    média = soma / 2
    print(f'{c:<8}{lista_geral[c][0]:<15}{média:<10}')
while True:
    notas = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe)'))
    if notas == 999:
        break
    if notas <= len(lista_geral) - 1:
        print(f'As notas de {lista_geral[notas][0]} são: {lista_geral[notas][1]}')



