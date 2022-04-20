banco_dados = []
grupo = []
qtd_pessoas = 0
while True:
    nome = str(input('Digite o nome:'))
    qtd_pessoas += 1
    peso = float(input('Digite o peso:'))
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('ERRO!Deseja continuar? [S/N]')).strip().upper()[0]
    banco_dados.append(nome)
    banco_dados.append(peso)
    grupo.append(banco_dados[:])
    banco_dados.clear()
    if cont == 'N':
        break
for c in grupo:
    if c[1] >= 100:
        print(f'As pessoas mais pesadas (Acima de 100kg) são: {c[0]}')
    if c[1] <= 70:
        print(f'As pessoas mais leves (menos que 70kg) são: {c[1]}')
print(f'{qtd_pessoas} pessoas cadastradas')


# CORRIGIR FORMATAÇÃO DA LISTAGEM