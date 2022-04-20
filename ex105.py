def notas(*notas, sit=0):
    """
    -> Função para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: (valor opcional) Indicando se deve ou não adicionar a sitação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    qtd = soma = 0
    dic = {}
    for num in notas:
        qtd += 1  # quantidade de notas
        soma += num  # soma das notas
        dic['total'] = qtd
        dic['maior'] = max(notas)  # maior nota
        dic['menor'] = min(notas)  # menor nota
        dic['média'] = soma / qtd  # média
    if dic['média'] >= 7 and sit != 0:
        dic['situação'] = 'boa'
    elif dic['média'] < 7 and sit != 0:
        dic['situação'] = 'ruim'
    return dic


# Programa principal
resp = notas(5.5, 9.5, 10)
print(resp)
