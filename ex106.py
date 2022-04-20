from time import sleep
c = ['\033[m',          # 0 = sem
     '\033[0:97:41m',   # 1 = vermelho
     '\033[0:97:42m',   # 2 = verde
     '\033[0:97:43m',    # 3 = amarelo
     '\033[0:97:44m',    # 4 = azul
     '\033[0:30:107m']   # 5 = branco

def minisist(msg):
     print(c[5], end='')
     help(msg)
     print(c[0], end='')
     sleep(.5)

def título(txt, cor=0):

    tam = len(txt)+4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')
    sleep(.5)


#Programa Principal
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    param = str(input('Função ou Biblioteca > '))
    if param.lower().strip() == 'fim':
        título('VOLTE SEMPRE', 1)
        break
    else:
        título(f'  Acessando o manual comando "{param}"...', 4)
        minisist(param)

