termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
for c in range(0,10):
    pa = termo + c*razao
    print(f'Termo {c+1} = {pa}')
