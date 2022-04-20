soma = 0 #acumulador
cont = 0 #contador
for impares in range(1, 500, 2):
    if impares % 3 == 0:
        cont = cont + 1
        soma = soma + impares
print(f'A soma de todos os {cont} é: {soma}.')

#COPIADO