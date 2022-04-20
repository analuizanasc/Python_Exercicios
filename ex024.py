#UMA OPÇÃO:
#nome =input('Qual o nome de sua cidade?')
#print('O nome da cidade começa com Santo')
#div = nome.split()
#print('SANTO' in div[0].upper())

nome = str(input('Qual o nome de sua cidade?'))
print( 'O nome de sua cidade começa com Santo \n{}.'.format(nome[:5].upper() == 'SANTO') )

