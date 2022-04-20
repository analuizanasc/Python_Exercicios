from random import randint
from time import sleep
jogos = {}
lista = []
print('Valores sorteados:')
for ref in range(1,5):
    jogos['jogadas'] = randint(1,6)
    print(f'    O jogador {ref} tirou {jogos["jogadas"]}')
    lista.append(jogos)
    sleep(.5)
print(lista)

#resolução do professor
'''from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),}
ranking = []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #itemgetter(1) > vai ordenar de acordo com o índice 1 do 'jogo'
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'O {i+1}o lugar: {v[0]} com {v[1]}')
    sleep(.5)'''