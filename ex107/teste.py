from ex107 import moeda

p = float(input('Digite o valor: R$'))
while True:
    q = int(input('Escolha a opção desejada:'
                  '\n [1] Metade'
                  '\n [2] Dobro'
                  '\n [3] Aumentar %'
                  '\n [4] Diminuir %'
                  '\n [5] Sair'
                  '\n Digite o número:'))
    while q != 1 and q != 2 and q != 3 and q != 4 and q !=5: #como simplificar?
        print('ERRO! Digite um número válido!')
        q = int(input(' [1] Metade'
                      '\n [2] Dobro'
                      '\n [3] Aumentar %'
                      '\n [4] Diminuir %'
                      '\n Digite o número:'))

    if q == 1:
        m = float(moeda.metade(p))
        print(f"A metade de R${p:.2f} é R${m:.2f}")
    elif q == 2:
        d = float(moeda.dobro(p))
        print(f'O dobro de R${p:.2f} é R${d:.2f}')
    elif q == 3:
        porc = float(input('Quantos porcentos você quer adicionar? [só números]'))
        resul = float(moeda.aumentar(p,porc))
        print(f'Aumentando {porc}% de {p}, temos R${resul:.2f}.')
    elif q == 4:
        porc = float(input('Quantos porcentos você quer diminuir? [só números]'))
        resul = float(moeda.diminuir(p,porc))
        print( f'Diminuindo {porc}% de {p}, temos R${resul:.2f}.')
    else:
        print(f'Volte Sempre!')
        break