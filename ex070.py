'''soma = mil = 0
lista = []
lista2 = []
while True:
    n = str(input('Nome do produto:'))
    p = float(input('Preço: R$'))
    lista2 += [n]
    soma += p
    lista += [p]
    barato = min(lista) #descobrir qual o item menor = mais barato!
    index = lista.index(barato) #posição na lista do item mais barato
    if p > 1000:
        mil += 1
    c = ' '
    while c not in 'SsNn':
        c = str(input('Deseja continuar? [S/N]')).strip()
    if c in 'Nn':
        break
nome = lista2[index] # identifica o nome na posição da lista (index)
print(f'O total gasto foi R${soma:.2f}')
print(f'{mil} produto(s) acima de 1000.00')
print(f'O produto mais barato foi: {nome}.')'''

soma = mil = qtd = menor = 0
nome = ' '
c = ' '
while True:
    n = str(input('Nome do produto:'))
    p = float(input('Valor: R$'))
    soma += p
    qtd += 1
    if p > 1000:
        mil += 1
    if qtd == 1:
        menor = p
        nome = n
    else:
        if p < menor:
            menor = p
            nome = n
    while c not in 'SsNn':
        c = str(input('Deseja continuar [S/N]:'))
    if c in 'Nn':
        break
print(f'O total foi: R$ {soma:.2f}.')
print(f'Produtos acima de R$1000,00: {mil}.')
print(f'Produto mais barato: {nome}.')