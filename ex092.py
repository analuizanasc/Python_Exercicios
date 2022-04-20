from datetime import date
dicionário = dict()
dicionário['nome'] = str(input('Digite o nome:'))
ano = int(input('Digite o ano de nascimento:'))
dicionário['idade'] = date.today().year - ano
dicionário['carteira'] = int(input('Digite a CTPS: (0 se não tiver)'))
if dicionário['carteira'] != 0:
    dicionário['contrato'] = int(input('Ano do contrato:'))
    dicionário['salário'] = int(input('Salário: R$'))
    dicionário['aposentadoria'] = (dicionário['contrato'] - ano) + 35
print('-=' * 30)
for k, v in dicionário.items():
    print(f'    -{k} tem o valor {v}')

