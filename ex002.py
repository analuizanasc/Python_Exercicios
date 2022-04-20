perg = input('Digite seu nome:')
print('Bem Vindo,',perg)
amarelo = '\033[30;43m'
branco = '\033[97m'
fim = '\033[m'
print(f'Bem Vindo, {amarelo} {perg} {fim}!')

#  cor      texto     fundo
# preto       30    >   40
# vermelho    31    >   41
# verde       32    >   42
# amarelo     33    >   43
# azul        34    >   44
# roxo        35    >   45
# cyan        36    >   46
# cinza       37    >   47
# branco      97    >  107


# estilo
# 0  > noone
# 1  > bold
# 4  > underline
# 7  > negative(invertir)