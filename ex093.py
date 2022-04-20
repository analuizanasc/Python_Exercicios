soma = 0
dicionário = {}
lista_gols = []
dicionário['nome'] = str(input('Digite o nome:')).strip().capitalize()
partidas = int(input(f'Quantas partidas {dicionário["nome"]} jogou?'))
for c in range(partidas):
    gols = int(input(f'Quantos gols na partida {c+1}?'))
    soma += gols
    lista_gols.append(gols)
dicionário['gols'] = lista_gols
dicionário['total'] = soma
print('=-' * 30)
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
print(f'Foi um total de {dicionário["total"]} gols.')