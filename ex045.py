'''from time import sleep
import random
print('Vamos jogar \033[35mJokenpô\033[m comigo!')
sleep(1)
print('\033[31mPedra...\033[m')
sleep(1)
print('\033[32mPapel...\033[m')
sleep(1)
print('\033[33mTesoura...\033[m')
sleep(1)
escolha = str(input('Escolha:').strip())
lista = ['pedra', 'papel', 'tesoura']
pc = str(random.choice(lista))
if escolha.upper() == 'PEDRA' and pc == 'tesoura':
    print(f'Eu escolhi {pc.lower()}. Pedra ganha de tesoura.')
elif escolha.upper() == 'PEDRA' and pc == 'papel':
    print(f'Eu escolhi {pc.lower()}. Pedra perde para papel!')
elif escolha.upper() == 'PEDRA' and pc.lower() == 'pedra':
    print(f'Eu escolhi {pc.lower()}. Deu empate!')

elif escolha.lower() == 'papel' and pc.lower() == 'pedra':
    print('Eu escolhi pedra. Papel ganha de pedra.')
elif escolha.lower() == 'papel' and pc.lower() == 'tesoura':
    print('Eu escolhi tesoura. Papel perde para tesoura.')
elif escolha.lower() == 'papel' and pc.lower() == 'papel':
    print('Empatamos!')

elif escolha.lower() == 'tesoura' and pc.lower() == 'papel':
    print('Eu escolhi papel. Tesoura ganha de pepel.')
elif escolha.lower() == 'tesoura' and pc.lower() == 'pedra':
    print('Eu escolhi pedra. Tesoura perde para pedra.')
elif escolha.lower() == 'tesoura' and pc.lower() == 'tesoura':
    print('Empatamos!')

else:
    print('Pedra? Papel? ou Tesoura?')'''

#REFAZENDO DE OUTRA FORMA...


from time import sleep
import random
print('Vamos jogar \033[35mJokenpô\033[m comigo!')
sleep(1)
print('\033[31mPedra...\033[m')
sleep(1)
print('\033[32mPapel...\033[m')
sleep(1)
print('\033[33mTesoura...\033[m')
sleep(1)
escolha = int(input('Escolha:'
                    '\n[0] Pedra'
                    '\n[1] Papel'
                    '\n[2] Tesoura'))
lista = ('pedra', 'papel', 'tesoura')
pc = random.randint(0,2)
if pc == 0:
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('VOCÊ VENCEU!')
    elif escolha == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('\033[1mJOGADA INVÁLIDA!\033[m')
if pc == 1:
    if escolha == 0:
        print('VOCÊ VENCEU!')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('\033[1mJOGADA INVÁLIDA!\033[m')
if pc == 2:
    if escolha == 0:
        print('COMPUTADOR VENCEU!')
    elif escolha == 1:
        print('VOCÊ VENCEU!')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('\033[1mJOGADA INVÁLIDA!\033[m')