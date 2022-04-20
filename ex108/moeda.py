def dobro(n):
    d = float((2 * n))
    return d


def metade(n):
    m = float((1/2 * n))
    return m


def aumentar(n,porc):
    a = float((n * (1+porc/100)))
    return a


def diminuir(n,porc):
    d = float(n * (1-porc/100))
    return d


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>4.2f}'.replace('.', ',')
