frase = str(input('Digite uma frase:')).upper().strip()
a = frase.count('A')
print("A letra 'A' aparece {} vezes.".format(a))
posi = frase.find('A')+1
print("A letra 'A' aparece primeiramente na posição {}.".format(posi))
print("A última letra 'A' apareceu na posição {}.".format(frase.rfind('A')+1))

#última posição do A????^^