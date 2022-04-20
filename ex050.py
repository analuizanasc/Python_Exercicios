s = 0
cont = 0
for c in range(1,4):
    perg = int(input('Digite um número inteiro:'))
    if perg % 2 == 0:
        s = s + perg
        cont += 1
print(f'Você informou {cont} números par(es) e a soma deles é: {s}.')
