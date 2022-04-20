## COPIADO
num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print(f'{num} convertido para binário é igual {bin(num)[2:]}.')
elif opção == 2:
    print(f'{num} convertido para octal é igual {oct(num)[2:]}.')
elif opção == 3:
    print(f'{num} convertido para hexadecimal é igual {hex(num)[2:]}')
else:
    print('Opção inválida!')