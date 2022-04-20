from datetime import date
menor = 0
maior = 0
for c in range (1,8):
    nasc = int(input(f'Que ano nasceu a {c} pessoa?'))
    idade = date.today().year - nasc
    if idade >= 21:
       maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoa(s) maiores de idade')
print(f'e  {menor} pessoa(s) menores de idade')

#copiado - não consegui fazer



##tentar novamente