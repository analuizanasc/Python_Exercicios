import math
ang = int(input('Digite um ângulo:'))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O seno de {ang} é {sin:.2f} \nO cosseno é {cos:.2f} \nA tangente é {tan:.2f}')
