'''maior = 0
menor = 0
for p in range(1, 4):
    peso = float(input(f'Qual o peso da pessoa {p}:'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg.')
print(f'O menor peso lido foi {menor}kg.')'''

lista = []
for c in range(1,5):
    peso = float(input(f'Qual o peso da pessoa {c}:'))
    lista += [peso]
print(f'O maior peso foi: {max(lista)} kg')
print(f'O menor peso foi: {min(lista)} kg')

