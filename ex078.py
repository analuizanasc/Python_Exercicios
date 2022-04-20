lista = []
lista_maior = []
lista_menor = []
for valores in range(0,5):
    num = int(input('Digite um número:'))
    lista.append(num)
for posição, valores in enumerate(lista):
    if valores == max(lista):
        lista_maior.append(posição)
    if valores == min(lista):
        lista_menor.append(posição)

print(f'Você digitou os números {lista}')
print(f'O maior valor é o {max(lista)} e está na posição {lista_maior}.')
print(f'O menor valor é o {min(lista)} e está na posição {lista_menor}.')