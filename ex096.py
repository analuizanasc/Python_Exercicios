def área(b, c):
    a = b*c
    print(f'A área de um terreno {b} x {c} é de {a}m2.')


#programa principal
largura = float(input('Largura (m):'))
comprimento = float(input('Comprimento (m):'))

área(largura, comprimento)
