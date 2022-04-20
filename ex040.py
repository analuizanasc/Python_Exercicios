nota1 = float(input('Digite a nota 01:'))
nota2 = float(input('Digite a nota 02:'))
media = ((nota1 + nota2) /2)
if media < 5:
    print('OPS! Você foi reprovado!')
elif 5 <= media <= 6.9:
    print('Você tem mais um chance... Está de recuperação!')
else:
    print('PARABÉNS! Você foi aprovado!')