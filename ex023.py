#uma opção:
#n = int(input('Digite um número entre 0 e 9999: '))
#n2 = str(int(10000 + n))
#print('O número {} possui, {} milhares.'.format(n, n2[1]))
#print('O número {} possui, {} centenas. '.format(n, n2[2]))
#print('O número {} possui, {} dezenas. '.format(n, n2[3]))
#print('O número {} possui, {} unidades.'.format(n, n2[4]))

perg = str(input('Digite o número entre 0 e 999:'))
num = perg.zfill(4)
print( 'O número {} possui: \nMilhar: {}\nCentena: {} \nDezena: {} \nUnidade: {}'.format(perg,num[0],num[1],num[2],num[3]))