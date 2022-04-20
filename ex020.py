'''from random import sample
n1 = input('Nome do aluno 01:')
n2 = input('Nome do aluno 02:')
n3 = input('Nome do aluno 03:')
n4 = input('Nome do aluno 04:')
print(sample([n1, n2, n3, n4], k=4))'''

from random import shuffle
n1 = input('Nome do aluno 01:')
n2 = input('Nome do aluno 02:')
n3 = input('Nome do aluno 03:')
n4 = input('Nome do aluno 04:')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:', lista)

