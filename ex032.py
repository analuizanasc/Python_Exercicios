from datetime import date
ano = int(input('Digite um ano(para o ano atual digite 0):'))
c1 = ano % 4
c2 = ano % 100
c3 = ano % 400
if ano == 0:
    ano = date.today().year
if c1 == 0 and c2 != 0 or c3 == 0:
    print(f'{ano} é ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')


## dando problema - analisar!
## dá certo com : if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: