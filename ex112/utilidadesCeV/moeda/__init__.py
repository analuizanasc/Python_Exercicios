def dobro(n=0,formato=False):
    d = float((2 * n))
    if formato:
        return moeda(d)
    return d


def metade(n=0, formato=False):
    m = float((1/2 * n))
    return m if not formato else moeda(m)


def aumentar(n=0, porc=0, formato=False):
    a = float((n * (1+porc/100)))
    return a if formato is False else moeda(a)


def diminuir(n=0 ,porc=0, formato=False):
    d = float(n * (1-porc/100))
    if moeda:
        return moeda(d)
    return d


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>4.2f}'.replace('.', ',')

def linha():
    print('-'*30)


def resumo(p=0, acresc=10, reduc=5):
    linha()
    print(f'RESUMO DO VALOR'.center(30))
    linha()
    print(f"Preço analisado: \t{moeda(p)}")
    print(f"Dobro do preço: \t{dobro(p, True)}")
    print(f"Metade do preço: \t{metade(p, formato=True)}")
    print(f"{acresc}% de aumento: \t{aumentar(p,acresc, formato=True)}")
    print(f"{reduc}% de redução: \t{diminuir(p, reduc, formato=True)}")
    linha()

