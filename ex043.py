altura = float(input('Digite sua altura:(m)'))
peso = float(input('Digite seu peso:(kg)'))
imc = peso / altura ** 2
print(f'Seu IMC é de {imc:.2f} kg/m².')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
else:
    print('Cuidado! Você está com obesidade mórbida!')