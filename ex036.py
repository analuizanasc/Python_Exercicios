valor = float(input('\033[1;32mQual o valor da casa?\033[m'))
salário = float(input('\033[1;31mQuanto é o seu salário?\033[m'))
anos = int(input('\033[1;34mQuantos anos você vai pagar a casa?\033[m'))

cond = 30/100*salário
prest = valor/(anos*12)

if (prest) >= (cond):
    print('Infelizmente, seu emprestimo foi negado!')
else:
    print('Parabéns! Seu emprestimo foi autorizado!')