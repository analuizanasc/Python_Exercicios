a = float(input('Diga o comprimento da primeira reta:'))
b = float(input('Diga o comprimento da segunda reta:'))
c = float(input('Diga o comprimento da terceira reta:'))
if a < b + c and b < a + c and c < a + b:
    print('As linhas formam um triângulo', end='')
    if a == b == c:
        print(' Equilátero!')
    if a != b != c != a:
        print(' Escaleno!')
    else:
        print(' Isósceles!')
else:
    print('Elas não podem formar um triângulo.')

## condições dentro de condições!!!!!

