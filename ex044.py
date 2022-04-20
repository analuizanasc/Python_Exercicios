preço = float(input('Digite o valor do produto:'))
pgmt = int(input('Digite o número correspondente à forma de pagamento:'
                 '\n(1) À vista no dinheiro ou Cheque '
                 '\n(2) À vista no cartão'
                 '\n(3) 2x no cartão'
                 '\n(4) 3x ou mais no cartão'))
vista = preço * 90/100
cartao = preço * 95/100
juros = preço * 120/100
if pgmt == 1:
    print(f'Você tem 10% de desconto. O novo valor do produto é: \033[32mR${vista:.2f}\033[m.')
elif pgmt == 2:
    print(f'Você tem um desconto de 5%. O novo valor é: \033[32mR${cartao:.2f}\033[m.')
elif pgmt == 3:
    print(f'O valor é: \033[32mR${preço:.2f}\033[32m.')
elif pgmt == 4:
    print(f'Você terá 20% de juros. O novo valor é: \033[32mR${juros:.2f}\033[m')
else:
    print('\033[1:31mOpção inválida de pagamento!\033[m')