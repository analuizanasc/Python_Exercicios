'''from random import choice
n1 = input('Nome do aluno 01:')
n2 = input('Nome do aluno 02:')
n3 = input('Nome do aluno 03:')
n4 = input('Nome do aluno 04:')
print(f' O aluno sorteado foi:', choice([n1, n2, n3, n4]))'''

from random import choice
n1 = input('Nome do aluno 01:')
n2 = input('Nome do aluno 02:')
n3 = input('Nome do aluno 03:')
n4 = input('Nome do aluno 04:')
lista = [n1, n2, n3, n4]
print(f'O aluno sorteado foi {choice(lista)}')