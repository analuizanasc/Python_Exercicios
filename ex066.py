soma = 0
qtd = 0
while True:
    n = int(input('Digite um número inteiro (999 para parar):'))
    if n == 999:
        break
    soma += n
    qtd += 1
print(f'{qtd} dígito(s) digitado(s)... A soma entre eles é: {soma}.')