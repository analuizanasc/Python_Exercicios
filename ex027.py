nome = str(input('Digite seu nome completo:'))
div = nome.split()
print('Seu primeiro nome é: {}.'.format(div.pop(0)))
print('Seu último nome é: {}.'.format(div.pop()))
 