sexo = str(input('Digite o sexo (F/M):')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo (F/M):')).strip().upper()[0]
print('FIM')