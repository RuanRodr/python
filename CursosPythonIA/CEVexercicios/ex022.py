nome = str(input('Digite seu nome:\n')).strip()

print(nome.upper())
print(nome.lower())
nomeSespaco = nome.replace(" ", "")
print(len(nomeSespaco))
print(nome.find(' '))