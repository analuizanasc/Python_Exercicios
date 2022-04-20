def leiaint(txt):
    a = input(txt)
    if a.isnumeric():
        return a
    while not a.isnumeric():
        print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
        a = input(txt)
        if a.isnumeric():
            return a
            break


#Programa principal
n = leiaint('Digite um número:')
print(f'Você acabou de digitar o número {n}.')