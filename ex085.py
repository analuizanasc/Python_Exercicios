'''lista_geral = []
pares = []
ímpares = []
for c in range(1,8):
    num = (int(input('Digite um númereo:')))
    if num % 2 == 0:
        pares.append(num)
        pares.sort()
    else:
        ímpares.append(num)
        ímpares.sort()

lista_geral.append(ímpares)
lista_geral.append(pares)

print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {ímpares}')'''

#OPÇÃO 2:
lista_geral = [[], []]
for c in range(1,8):
    valor = int(input(f'Digite o {c}o. valor:'))
    if valor % 2 == 0:
        lista_geral[0].append(valor)
    else:
        lista_geral[1].append(valor)
lista_geral[0].sort()
lista_geral[1].sort()
print(f'Os valores pares digitados foram: {lista_geral[0]}')
print(f'Os valores ímpares digitados foram: {lista_geral[1]}')