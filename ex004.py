info = input('Digite algo: ')
print(f'Você escreveu: {info}')
print(f'\033[4m{info}\033[m é alfanumérico?', info.isalnum())
print(f'\033[4m{info}\033[m é numérico?', info.isnumeric())
print('Ele está em caixa baixa? ', info.islower())
print('\033[4m{}\033[m está em caixa alta?'.format(info), info.isupper())
print(f'\033[4m{info}\033[m é decimal?', info.isdecimal())
print(f'\033[4m{info}\033[m é imprimível?', info.isprintable())
print(f'\033[4m{info}\033[m é termo alfabético?', info.isalpha())
print(f'\033[4m{info}\033[m é um título?', info.istitle())
print(f'\033[4m{info}\033[m é um dígito?', info.isdigit())
print(f'\033[4m{info}\033[m é identificador?', info.isidentifier())
print('Fim!!!!')