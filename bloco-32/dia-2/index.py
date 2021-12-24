# Exercício 1 - imprimir nome na vestical em escada invertida

def printName(name):
    i = len(name)

    while i > 0:
        print(name[0:i])
        i -= 1


printName('PEDRO')
