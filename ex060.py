'''from math import prod
num = int(input('Digite um número:'))
c = 0
lista =[]
while c < num:
    c += 1
    lista += [c]
produto = prod(lista)
print(f'{num}! = {produto}')'''



'''from math import factorial
num = int(input('Digite um número:'))
fat = factorial(num)
print(f'{num}! = {fat}')'''



num = int(input('Digite um número:'))
c = num
f = 1
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)
