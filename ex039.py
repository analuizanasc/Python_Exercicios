from datetime import date
gender = str(input('Você '))
ano = int(input('Boy, que ano você nasceu?'))
idade = date.today().year - ano
atraso = idade - 18
prazo = 18 - idade
if idade == 18:
    print('\033[031mEstá na hora de se alistar!\033[m')
elif idade > 18:
    print(f'Eita! Você passou \033[32m{atraso} anos(s)\033[m do tempo de se alistar!')
elif idade<18:
    print(f'Falta \033[32m{prazo} ano(s)\033[m  para você se alistar!')