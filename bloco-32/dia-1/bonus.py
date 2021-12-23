# Exercício 1 - menor elemento da lista

def minValue(list):
    print(min(list))


# minValue([5, 9, 3, 19, 70, 8, 100, 2, 35, 27])

# Exercício 2 - criar triângulo com n astericos

def createTriangle(n):
    for i in range(n):
        print((i + 1) * '*')


# createTriangle(5)

# Exercício 3 - retornar soma de determinado intervalo de numeros

def sumNumbers(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i

    print(sum)


# sumNumbers(5)

# Exercício 4 - calcular valor pago pela gasolina

def amountPaidForFuel(liters, type):
    prices = {
        'G': 2.50,
        'A': 1.90
    }

    price = liters * prices[type]

    discounts = {
        'G': lambda value:
        value - value * 0.03 if liters <= 20 else value - value * 0.05,
        'A': lambda value:
        value - value * 0.04 if liters <= 20 else value - value * 0.06
    }

    print(discounts[type](price))


amountPaidForFuel(25, 'A')
