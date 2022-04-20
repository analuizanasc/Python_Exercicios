'''termo = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão:'))
conta = 0
while conta <= 10:
    conta+= 1
    pa = termo + conta * razão
    print(f'Termo {conta}: {pa}')'''

primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão:'))
termo = primeiro
conta = 1
while conta <= 10:
    print(f'{termo} - ', end='')
    termo += razão
    conta += 1
print('FIM')

