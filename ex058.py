import time
import random
print('-'*70)
print('Vamos brincar? Vou pensar em um número entre 0 e 10... Tente adivinhar!')
print('-'*70)
time.sleep(1)
num = 0
conta = 0
pc = int(random.randint(0,10)) # fazer o pc 'pensar'em um número
while num != pc:
    num = int(input('Digite o número que estou pensando (entre 0 e 10):'))
    conta += 1 # cada tentativa errada conta +1 (iniciando no 0 -> conta = 0)
    if pc < num:
        print('\033[33mUm pouco menos...\033[m')
    elif pc > num:
        print('\033[33mUm pouco mais...\033[m')
print('\033[31mACERTOU!!\033[m')
print(f'Você acertou na tentativa {conta}!')

'''from random import randint
pc = randint(0,10)
print('Sou seu computador... Acabei de pendar em um número entre 0 e 10.')
print('Será que você consegue adivinhasr qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite?'))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if pc < jogador:
            print('\033[33mUm pouco menos...\033[m')
        elif pc > jogador:
            print('\033[33mUm pouco mais...\033[m')
print(f'\033[1:31mParabéns!\033[m Você acertou com {palpites} tentativas.')'''