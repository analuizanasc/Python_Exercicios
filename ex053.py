''''frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')'''

'''#outra forma:
frase = str(input('Digite uma frase (desconcidere acentos):')).strip().split()
junto = ''.join(frase).upper()
inverso = frase[::-1]
if inverso == frase:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')'''

frase = str(input('Digite uma frase (desconcidere acentos):')).upper().replace(" ","")
print(frase)
junto = frase[::-1]
if frase == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')

