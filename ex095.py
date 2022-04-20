soma = 0
dicionário = {}
lista_gols = []
lista2_gols = []
while True:
    dicionário['nome'] = str(input('Digite o nome:')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {dicionário["nome"]} jogou?'))
    for c in range(partidas):
        gols = int(input(f'Quantos gols na partida {c+1}?'))
        soma += gols
        lista_gols.append(gols)
        lista_gols.clear()
        dicionário['gols'] = lista_gols
        dicionário['total'] = soma
        lista2_gols.append(dicionário.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO!Deseja continuar? [S/N]')
    if continuar == 'N':
        break
    print('=' * 30)
    if continuar == 'N':
        break
print(lista2_gols)
print(dicionário)

'''print('=-' * 30)
print(dicionário)
print('=-' * 30)
for k, v in dicionário.items():
    print(f'O campo {k} tem valor {v}.')
print('=-' * 30)
print(f'O jogador {dicionário["nome"]} jogou {partidas} partidas.')
index = 0
for v in lista_gols:
    print(f'    =>Na partida {index+1}, fez {v} gols.')
    index += 1
print(f'Foi um total de {dicionário["total"]} gols.')'''