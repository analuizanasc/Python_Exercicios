n1 = int(input('\33[35mDigite um número:\033[m'))
n2 = int(input('\033[35mDigite outro número:\033[m'))
s = n1+n2
print(f'A soma de \033[32m{n1}\033[m e \33[32m{n2}\33[m é \033[4m{s}\033[m')



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