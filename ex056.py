soma = 0
conta_mulh = 0
lista_idade = []
lista_nome = []
for a in range(1,5):
    nome = str(input(f'Digite o nome da pessoa {a}:'))
    idade = int(input(f'Digite a idade da pessoa {a}:'))
    sexo = str(input(f'Digite o sexo da pessoa {a}: \n(F)Feminino \n(M)Masculino')).strip().upper()
    soma += idade
    if sexo == 'F' and idade < 20:
        conta_mulh += 1
    if sexo == 'M':
        lista_idade += [idade] #lista com idades
        lista_nome += [nome] #lista com nomes
        mais_velho = max(lista_idade) #identificar quem é o mais velho
        index = lista_idade.index(mais_velho) #posição na lista do mais velho
        nome_velho = lista_nome[index] #identifica o nome pela posição do index(mais velho)
print(f'O nome do homem mais velho é:{nome_velho}.')
print(f'O grupo possui {conta_mulh} mulher(es) abaixo de 20 anos.')
print(f'A média de idade do grupo é: {soma/4:.0f} anos.')
