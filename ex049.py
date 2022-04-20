n = int(input('Digite um número inteiro:'))
print('\033[35m-\033[m'*8)
print('\033[35mTABUADA\033[m')
print('\033[37m-\033[m'*8)
for tab in range(1,11):
   res = n*tab
   print(f'{n} x {tab} = {res}')
  # print(n,'*',tab,'=',res)

