'''num = 0
lista = []
conta = 0
while num != 999:
    num = int(input('Digite um número (999 para parar):'))
    lista += [num] #lista com os números digitados
    conta += 1 #quantidade de núumeros digitados
soma = sum(lista) - 999
print(f'{conta -1} números foram digitados. \nA soma entre eles é: {soma}.')'''

num = conta = soma = 0
num = int(input('Digite um número (999 para parar):'))
while num != 999:
    soma += num #soma dos números
    conta += 1 #quantidade de números digitados
    num = int(input('Digite um número (999 para parar):'))
print(f'{conta} números foram digitados. \nA soma entre eles é: {soma}.')