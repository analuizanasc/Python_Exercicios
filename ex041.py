from datetime import date
data = int(input('Informe sua data de nascimento:'))
idade = date.today().year - data
if idade <= 9:
    print('Você é da categoria \033[34mMIRIM\033[m.')
elif idade <= 14: # pode colocar assim tb : 10 <= idade < 14
    print('Você é da categoria \033[34mINFANTIL\033[m.')
elif idade <= 19:
    print('Você está na categoria \033[34mJUNIOR\033[m.')
elif idade <= 25:
    print('Você está na categoria \033[34mSÊNIOR\033[m.')
else:
    print('Você está na categoria \033[34mMASTER\033[m.')