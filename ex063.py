print('-' * 25)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 25)
n = int(input('Quantos termos você deseja ver?'))
t1 = 0
t2 = 1
print(f'{t1} {t2}', end=" ")
seq = 3
while seq <= n:
    t3 = t1 + t2
    print(f'{t3}', end=" ")
    t1 = t2
    t2 = t3
    seq += 1
print('FIM')



#fazer depois