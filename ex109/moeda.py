def dobro(n=0,formato=False):
    d = float((2 * n))
    if formato:
        return formato(d)
    return d


def metade(n=0, formato=False):
    m = float((1/2 * n))
    return m if not formato else formato(m)


def aumentar(n=0, porc=0, formato=False):
    a = float((n * (1+porc/100)))
    return a if formato is False else moeda(a)


def diminuir(n=0 ,porc=0, formato=False):
    d = float(n * (1-porc/100))
    if moeda:
        return formato(d)
    return d


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>4.2f}'.replace('.', ',')
