'''continuar = ""
lista = []
qtd = 0
while continuar != 'N':
    num = int(input('Digite um número inteiro:'))
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    lista += [num]
    qtd += 1
média = sum(lista)/qtd
maior = max(lista)
menor = min(lista)
print(f'A média dos valores é: {média:.0f}, o maior número digitado foi: {maior} e o menor: {menor}.')'''

resp = 'S'
soma = qtd = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número:'))
    resp = str(input('Quer continuar: [S/N]')).strip().upper()[0] #[0] => considerar somente a primeira letra (string)
    soma += n
    qtd += 1
    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
média = soma/qtd
print(f'Você digitou {qtd} números e a média foi {média} '
      f'\nO maior valor foi {maior} e o menor foi {menor}')


