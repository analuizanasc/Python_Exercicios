conta = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0:
        fim = '\033[1:31mPROGRAMA FINALIZADO!\033[m'
        print(f'{fim:^40}')
        break
    for conta in range(1,11):
        tabuada = n * conta
        print(f'{conta} x {n} =', tabuada)
