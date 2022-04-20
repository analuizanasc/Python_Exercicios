def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
       return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Que ano você nasceu?'))
print(voto(nasc))

