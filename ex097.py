def escreva(txt):
    print('-' * (len(txt)+4))
    print(f'  {txt}  ')
    print('-' * (len(txt)+4))


txt = str(input('Digite o texto:'))
escreva(txt)