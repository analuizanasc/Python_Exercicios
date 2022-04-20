while True:
     extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                'dezenove', 'vinte')
     n = int(input('Digite um número de 0 a 20:'))
     while n < 0 or n > 20:
          n = int(input('ERRO! Digite novamente um número de 0 a 20:'))
     print(f'Você digitou: {extenso[n].upper()}')
     c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
     while c not in 'SN':
          c = str(input('ERRO! Deseja continuar? [S/N]')).strip().upper()[0]
     if c == 'N':
          break

'''import n2w as n2w
n = int(input('Digite um número de 0 a 20:'))
print(n2w.convert(n))'''

