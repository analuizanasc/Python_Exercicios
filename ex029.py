vel = float(input(('Digite a velocidade do carro (em km/h):')))
if vel > 80:
    print('Você foi multado!')
    mais = vel - 80
    valor = float(mais * 7)
    print(f'A multa custará R${valor:.2f}.')
print('Tenha um bom dia!')
