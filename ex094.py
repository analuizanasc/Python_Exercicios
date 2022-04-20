dicionário = {}
lista = []
quantidade = soma_idades = 0
while True:
    dicionário['nome'] = str(input('Digite o nome:')).strip().capitalize()
    dicionário['sexo'] = str(input('Digite o sexo: [F/M]')).strip().upper()[0]
    dicionário['idade'] = int(input('Digite a idade:'))
    quantidade += 1
    soma_idades += dicionário['idade']
    média = soma_idades / quantidade
    lista.append(dicionário.copy())
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('ERRO!Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(lista)
print(f'{quantidade} foram cadastradas.')
print(f'A média de idades é {média:5.2f} anos.')
print(f'As mulheres são: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p["nome"], end=' ')
print()
print(f'As pessoas acima da média são: ', end='')
for p in lista:
    if p['idade'] >= média:
        print(p['nome'], end='')