from functools import reduce
from math import ceil

# Exercício 1 - maior número


def higherNumber(a, b):
    if a > b:
        return a
    else:
        return b


number = higherNumber(10, 15)

# Exercício 2 - média aritimérica


def arithmeticAverage(list):
    sumValues = reduce(lambda a, b: a + b, list)

    return sumValues / len(list)


average = arithmeticAverage([10, 200, 25, 2])

# Exercício 3 - quadrado de asteriscos


def createSquare(n):
    square = ''

    for i in range(n):
        str = n * '*'

        square += str + '\n'
    return square


square = createSquare(4)


# Exercício 4 - maior nome da lista

def higherName(list):
    name = reduce(lambda a, b: a if len(a) > len(b) else b, list)

    return name


name = higherName(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])


# Exercício 5 - calcula quantidade de tinta e valor

def calculateInkAndPrice(metters):
    inkQuantity = metters / 3

    cans = ceil(inkQuantity/18) if inkQuantity > 18 else 1

    return (cans, "R$ {:.2f}".format(cans * 80))


ink = calculateInkAndPrice(250)


# Exercício 6 - verifica tipo de triângulo

def checkTriangleType(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print('Não é triângulo')
    elif a == b == c:
        print('Triângulo Equilátero')
    elif a == b or a == c or b == c:
        print('Triângulo Isóceles')
    elif a != b != c:
        print('Triângulo Escaleno')


checkTriangleType(2, 3, 4)
