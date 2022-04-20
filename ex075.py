lista = []
for n in range(0,5):
    n = int(input('Digite um número:'))
    lista.append(n) # add os elementos na lista
tupla = tuple(lista) #transformar uma lista em tupla

qtd = tupla.count(9)
posição = tupla.index(3)


print(f'O 9 aparece {qtd+1} vezes.')
print(f'O 3 aparece primeiro na posição {posição}.')


#FALTOU O ÚLTIMO -> PARES
#corrigir : erro qndo não tem 3 na tupla



