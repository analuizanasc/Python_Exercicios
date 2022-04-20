dicionário = {}
dicionário['Nome'] = str(input('Digite o nome:'))
dicionário['Média'] = float(input('Digite a média:'))
if dicionário['Média'] >= 7:
    dicionário['Situação'] = 'Aprovado'
elif 5 <= dicionário['Média'] < 7:
    dicionário['Situação'] = 'Recuperação'
else:
    dicionário['Situação'] = 'Reprovado'
print('=-'*30)
for k, v in dicionário.items():
    print(f'{k} é igual a {v}')
print('=-'*30)