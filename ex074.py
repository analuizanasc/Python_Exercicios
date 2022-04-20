''' TENTATIVA 01:
from random import randint
print('Números:', end=" ")
for pc in range(1,5):
    pc = int(randint(0,10))
    tupla = (pc)'''


'''from random import randint
pc1 = randint(0,10)
pc2 = randint(0,10)
pc3 = randint(0,10)
pc4 = randint(0,10)
pc5 = randint(0,10)
tupla = pc1 , pc2 , pc3, pc4, pc5
print(f'Números aleatórios: {tupla}')
menor = min(tupla)
maior = max(tupla)
print(f'Menor número: {menor}')
print(f'Maior número: {maior}')'''

from random import randint
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Números aleatórios:', end = " ")
for c in tupla:
    print(c, end=" ")
menor = min(tupla)
maior = max(tupla)
print(f'\nMenor número: {menor}')
print(f'Maior número: {maior}')