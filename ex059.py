from time import sleep
valor_1 = int(input('Digite um valor:'))
valor_2 = int(input('Digite outro valor:'))
menu = 0
while menu != 5:
    sleep(1)
    print('-'*30)
    menu =int(input('Digite a opção:'
                     '\n\033[1m[1]somar'
                     '\n[2]multiplicar'
                     '\n[3]maior'
                     '\n[4]novos números'
                     '\n[5]sair do programa\033[m'))
    if menu == 1:
        print(f'{valor_1} + {valor_2} = {valor_1 + valor_2}')
    elif menu == 2:
        print(f'{valor_1} x {valor_2} = {valor_1*valor_2}')
    elif menu == 3:
        lista_num = [valor_1,valor_2]
        print(f'O maior número é: {max(lista_num)}')
    elif menu == 4:
        print('Informe os números novamente:')
        valor_1 = int(input('Digite um valor:'))
        valor_2 = int(input('Digite outro valor:'))
    elif menu == 5:
        print('\033[31mVocê saiu do programa!\033[m')
    else:
        print('Opção inválida!')

