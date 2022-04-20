from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    linhas()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    cont = cont2 = i
    while cont <= f:
        print(cont, end=' ')
        cont += p
        sleep(.5)

    while cont2 >= f:
        print(cont2, end=' ')
        cont2 -= p
        sleep(.5)
    print()

def linhas():
    print('=-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
linhas()
print('Agora é sua vez de personalizar a contagem:')
i = int(input('     Início:'))
f = int(input('     Fim:'))
p = int(input('     Passo:'))
contador(i, f, p)
