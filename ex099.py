def maior(*num):
    if num == 0:
        print('O maior valor ')
        return
    print('=-'*30)
    print('Analisando os valores passados...')
    lista = [*num]
    for num in lista:
        print(num, end=' ')
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()




#faltou o  maior()