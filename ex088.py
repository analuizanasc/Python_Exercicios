from random import randint
from time import sleep
print('='*50)
print(f'{"JOGO DA MEGA SENA":^50}')
print('='*50)
qtd = int(input('Quantos jogos você que que eu sorteie?'))
tot = 1
lista = []
jogos = []
while tot <= qtd:
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
        if len(lista) == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-'*25)
print(f'{"SORTEANDO JOGOS":^50}')
print('=-'*25)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(.5)