tupla = ( 'Atlético- MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
          'Fluminense', 'América- MG', 'Atlético- GO', 'Santos', 'Ceará', 'Internacional',
          'São Paulo', 'Athletico- PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport',
          'Chapecoense')
print(f'Os cinco primeiros colocados são: {tupla[0:5]}.')
print('='*70)
print( f'Os últimos quatro colocados são: {tupla[-4:]}.')
print('='*70)
print(f'Os 20 primeiros colocados do Brasileirão em ordem alfabética são: {sorted(tupla)}.')
print('='*70)
posição = tupla.index('Chapecoense') + 1
print(f'O time Chapecoense está na posição {posição}.')
