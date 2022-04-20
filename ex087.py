'''lista = []
lista_maior = []
soma = 0
for c in range(1,10):
    num = int(input(f'Digite número {c}:'))
    lista.append(num)
    if num % 2 == 0:
        soma += num
lista_maior.append(lista[3])
lista_maior.append(lista[4])
lista_maior.append(lista[5])

print('A Matriz dos números dados é:')
print(f'[{lista[0]}] [{lista[1]}] [{lista[2]}]')
print(f'[{lista[3]}] [{lista[4]}] [{lista[5]}]')
print(f'[{lista[6]}] [{lista[7]}] [{lista[8]}]')
print(f'A soma dos valores pares digitados é: {soma}')
print(f'A soma dos valores da terceira coluna é: {lista[1] + lista[4] + lista[7]}')
print(f'O maior valor da segunda linha é: {max(lista_maior)}')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somacol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
for l in range(0,3):
    somacol += matriz[l][2] #outra opção de fazer soma da terceira coluna
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares digitados é: {soma}')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
print(somacol)