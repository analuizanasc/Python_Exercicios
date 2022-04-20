import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso!')
    print(site.read()) # mostra o site - lembrando que nesse caso o site é a variável definida anteriormente