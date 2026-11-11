import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except urllib.error.URLError:
    print('o site não está acessivel')
else:
    print('Tudo ok')
    print(site.read())
    print(site.code)
    print(site.url)