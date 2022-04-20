import random
import time
num = int(random.randint(0,5))
print('-'*70)
print('Vamos brincar? Vou pensar em um número entre 0 e 5... Tente adivinhar!')
print('-'*70)
time.sleep(1)
perg = int(input('Que número estou pensando?'))
print('Será???')
time.sleep(1)
if perg == num:
    print('PARABÉNS! VOCÊ ACERTOU!')
else:
    print('OOHH, NÃO! TENTE DE NOVO!!!')
