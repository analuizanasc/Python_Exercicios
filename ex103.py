def ficha(n, g):
        if n.strip()== '':
                n='<desconhecido>'
        if g=='':
                g=0
        elif g!=0:
                if g[0] not in '0123456789':
                        g=0
        return f'{n} fez {g} gols'


#Programa principal
nome = str(input('Digite o nome do jogador:')).capitalize().strip()
gols = str(input(f'Gols marcados:')).strip()
print(ficha(nome, gols))
