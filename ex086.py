'''# OPÇÃO 01
lista01 = []
lista02 = []
lista03 = []
lista04 = []
lista05 = []
lista06 = []
lista07 = []
lista08 = []
lista09 = []
num01 = int(input('Digite [0,0]:'))
lista01.append(num01)
num02 = int(input('Digite [0,1]:'))
lista02.append(num02)
num03 = int(input('Digite [0,2]:'))
lista03.append(num03)
num04 = int(input('Digite [1,0]:'))
lista04.append(num04)
num05 = int(input('Digite [1,2]:'))
lista05.append(num05)
num06 = int(input('Digite [1,3]:'))
lista06.append(num06)
num07 = int(input('Digite [2,0]:'))
lista07.append(num07)
num08 = int(input('Digite [2,1]:'))
lista08.append(num08)
num09 = int(input('Digite [2,2]:'))
lista09.append(num09)

print(lista01, lista02, lista03)
print(lista04, lista05, lista06)
print(lista07, lista08, lista09)'''

'''#OPÇÃO 02
lista = []
lista2 = []
lista3 = []
for c in range(1,4):
    num = int(input(f'Digite [0,{c}]:'))
    lista.append(num)
for c in range(1,4):
    num = int(input(f'Digite [1,{c}]:'))
    lista2.append(num)
for c in range(1,4):
    num = int(input(f'Digite [2,{c}]:'))
    lista3.append(num)
print(f'[{lista[0]}] [{lista[1]}] [{lista[2]}]')
print(f'[{lista2[0]}] [{lista2[1]}] [{lista2[2]}]')
print(f'[{lista3[0]}] [{lista3[1]}] [{lista3[2]}]')'''

#OPÇÃO DO PROFESSOR:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() # quando terminar a coluna, ele quebra e forma linha
