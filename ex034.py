perg = float(input('Quanto você ganha de salário?'))
aum1 = (perg + (10/100*perg))
aum2 = (perg + 15/100*perg)
if perg >= 1250:
    print(f'Você ganhou um aumento! Seu novo salário será: R${aum1:.2f}.')
else:
    print(f'Você ganhou um aumento! Seu salário agora será: R${aum2:.2f}.')