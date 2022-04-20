n = int(input('Digite um número inteiro:'))
n1 = n*1
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n*10
print(f'Sua tabuada é: \n {n}*1={n1} \n {n}*2={n2} \n {n}*3={n3} \n {n}*4={n4} \n {n}*5={n5} \n {n}*6={n6} \n {n}*7={n7} \n {n}*8={n8} \n {n}*9={n9} \n {n}*10={n10}')

# outra forma de fazer a tabuada:
print('Sua tabuada é:')
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')