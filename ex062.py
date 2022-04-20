'''termo = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão:'))
conta = 0
while conta < 10:
    conta+= 1
    pa = termo + conta * razão
    print(f'Termo {conta}: {pa}')
mais = ''
while mais != 'N':
    mais = str(input('Você quer outro termo? [S/N]')).strip().upper()
    if mais == 'S':
        termo_extra = int(input('Qual termo?'))
        pa2 = termo + termo_extra * razão
        print(f'Termo {termo_extra}: {pa2}')
else:
    print('OK!')'''

primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão:'))
termo = primeiro
conta = 1
total = 0
mais = 10
print('PA = ', end=" ")
while mais != 0:
    total += mais
    while conta <= total:
        print(termo, end=" ")
        termo += razão
        conta += 1
    mais = int(input('\nQuantos você quer mostrar mais?'))
print(f'Progressão finalizada com {total} termos mostrados.')

#estudar novamente!!!!!!!!!