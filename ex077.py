tupla = ('Ana', 'Luiza', 'Araujo', 'do', 'Nascimento')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} tem as vogais:', end= "")
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end= " ")

#como fazer se tiver repetido as letras? Não repetir!