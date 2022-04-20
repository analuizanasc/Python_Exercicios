def leiadinheiro(msg):
    while True:
        comando = str(input(msg)) .strip().replace(',', '.')
        if comando.isalpha() or comando == '':
            print(f'\033[31mERRO: "{comando}" não é uma mensagem válida\033[m')
        else:
            return float(comando)
            break



