from ex109 import moeda

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
        m = moeda.metade(p, formato=True)
        print(f'A metade de {moeda.moeda(p)} é {m}')
    elif q == 2:
        d = moeda.dobro(p, formato=True)
        print(f'O dobro de {moeda.moeda(p)} é {d}')
    elif q == 3:
        porc = float(input('Quantos porcentos você quer adicionar? [só números]'))
        resul = moeda.aumentar(p,porc, formato=True)
        print(f'Aumentando {porc}% de {moeda.moeda(p)}, temos {resul}.')
    elif q == 4:
        porc = float(input('Quantos porcentos você quer diminuir? [só números]'))
        resul = moeda.diminuir(p,formato=porc)
        print(f'Diminuindo {porc}% de {moeda.moeda(p)}, temos {resul}.')
    else:
        print(f'Volte Sempre!')
        break