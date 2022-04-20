perg = float(input('Oi, qual será a distância da viagem (em km)?'))
'''if perg <= 200:
    print(f'Sua passagem será R${float(perg*0.50):.2f}.')
else:
    print(f'Sua passagem será R${float(perg*0.45):.2f}')'''

''' OUTRA OPÇÃO!!!!!!
if perg <= 200:
    preço = perg * 0.5
else:
    preço = perg * 0.45
print(f'Sua passagem custará: R${preço:.2f}.')'''

preço = perg *0.5 if perg <= 200 else perg*0.45
print(f'O valor da passagem é: R${preço:.2f}')