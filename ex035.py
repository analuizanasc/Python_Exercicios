a = float(input('Diga o comprimento da primeira reta:'))
b = float(input('Diga o comprimento da segunda reta:'))
c = float(input('Diga o comprimento da terceira reta:'))
p1 = a + b
p2 = a + c
p3 = b + c
p4 = p1 > c
p5 = p2 > b
p6 = p3 > a
if p4 == p5 == p6:
    print('As retas formam um triângulo!')
else :
    print('As retas não podem formar um tirângulo!')

'''OUTRA FORMA!!
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar um triângulo!') '''
