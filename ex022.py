frase = str(input('Olá! Qual o seu nome?')).strip()
print('Seu nome em maiúsculo é {}.'.format(frase.upper()))
print('Seu nome em minúsculo é {}.'.format(frase.lower()))
print('Seu nome tem {} letras.'.format(len(frase)-frase.count(' ')))
dividido = frase.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))

