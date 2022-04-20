dias = int(input('E quantos dias você ficou como carro?'))
km = float(input('Oi, quantos quilometros você percorreu?'))
vd = 60*dias
vkm = 0.15*km
print(f'O valor final é: R$ {vd+vkm:0.2f}.')