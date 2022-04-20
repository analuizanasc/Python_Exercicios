from random import randint


def sorteia():  # sorteia números e coloca na lista
    números = []
    print(f'A lista sorteada foi:', end= ' ')
    for num in range(1, 6):
        n = randint(1, 100)
        números.append(n)
        print(n, end=' ')
    print()
    def somapar():
        listapar = []
        for num in números:
            if num % 2 == 0:
                listapar.append(num)
        print(f'A soma de todos os valores pares {listapar} da lista é: {sum(listapar)}')
    somapar()


sorteia()
