def fatorial(n, show=False):
    """
    > Calcula o fatorial de um número.
    :param n: número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n
    """
    fat = 1
    for p in range(n, 0, -1):
        if show:
            print(f'{p}', end=' ')
            if p > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        fat *= p
    return fat


n = int(input('Digite um número:'))
print(fatorial(n))
