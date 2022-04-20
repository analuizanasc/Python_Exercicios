num1 = int(input('\033[32mDigite um número inteiro:'))
num2 = int(input('Digite outro número inteiro:'))
if num1 > num2:
    print('O \033[35mprimeiro número\033[m \033[032mé maior!')
elif num2 > num1:
    print('O \033[36msegundo número\033[m \033[032mé maior!')
elif num1 == num2: #ou else:
    print(f'\033[31mOs números são iguais!\033[m')