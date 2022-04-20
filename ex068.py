import random
print('Vamos brincar de par ou ímpar?')
vzs = 0
while True:
    pc = random.randint(0, 11)
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]')).strip().upper()
    n = int(input('Digite um número:'))
    soma = n + pc
    print(f'Você jogou {n} e o computador {pc}.')
    print(f'{soma} é', 'PAR' if soma % 2 == 0 else 'ÍMPAR')
    if soma % 2 == 0:
        if tipo == 'P':
            print('Você ganhou!')
            vzs += 1
        else:
            print('Perdeu, playboy!')
            break
    else:
        if tipo == 'I':
            print('Você ganhou!')
            vzs += 1
        else:
            print('Perdeu, playboy!')
            break
print(f'Você ganhou {vzs} vezes. GAME OVER!')



#refeito após vídeo
