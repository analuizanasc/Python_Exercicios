n1 = float(input('Digite a nota 01 do aluno:'))
n2 = float(input('Digite a nota 02 do aluno:'))
md = (n1+n2)/(2)
if md < 7:
    print(f'A média do aluno é: \033[31m{md:.1f}')
else:
    print(f'A média do aluno é: \033[32m{md:.1f}')



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