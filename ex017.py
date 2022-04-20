'''from math import (sqrt)
co = float(input('Qual o comprimento do cateto oposto de seu triângulo retângulo?'))
ca = float(input('Qual o comprimento do cateto adjacente de seu triângulo retângulo?'))
hip = float(sqrt((co**2+ca**2)))
print(f'O comprimento da hipotenusa de seu triângulo retângulo é {hip:.0f}')'''

from math import hypot
co = float(input('Qual o cateto oposto?'))
ca = float(input('Qual o cateto adjacente?'))
print(f'A hipotenusa é {hypot(co,ca):.2f}')