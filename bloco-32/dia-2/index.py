import random
import json
import csv
# Exercício 1 - imprimir nome na vestical em escada invertida


def printName(name):
    i = len(name)

    while i > 0:
        print(name[0:i])
        i -= 1


# printName('PEDRO')

# Exercício 2 - Jogo da palavra embaralhada.

def scrambledWordGame(words):
    randomWord = random.choice(words)
    wordChars = list(randomWord)
    random.shuffle(wordChars)
    scrambled_word = ''.join(wordChars)

    rounds = 3

    while rounds > 0:
        print(scrambled_word)
        response = input('Qual a palavra embaralhada acima?\n')
        print()

        if rounds == 1 and response != randomWord:
            print('A palavra certa era {}. Você perdeu!'.format(randomWord))
            print()
            break
        elif response != randomWord:
            print('Palavra errada. Tentativas restantes {}'.format(rounds - 1))
            print()
        else:
            print('Parabéns, palavra correta.')
            break

        rounds -= 1


# scrambledWordGame(['Janaina', 'Comer', 'Vacina'])

# Exercício 3 - Buscar palavras para o exercício 2 de um arquivo

def readWordsFile():
    file = open('words.txt', 'r')
    words = file.read().split('\n')
    return words


# words = readWordsFile()
# scrambledWordGame(words)


def readJsonFile():
    with open('books.json', 'r') as file:
        data = json.load(file)

    return data


def groupBooks(list):
    books = {}
    totalBooks = 0

    for item in list:
        if len(item['categories']):
            for category in item['categories']:
                if category == '':
                    break

                totalBooks += 1

                if category in books:
                    books[category].append(item)
                else:
                    books[category] = [item]
        else:
            if 'noCategory' in books:
                books['noCategory'].append(item)
            else:
                books['noCategory'] = [item]

    return (books, totalBooks)


def booksPercentageByCategory(booksByCategories, totalBooks):
    keys = booksByCategories.keys()
    countedBooks = map(lambda key: dict({
        'categoria': key,
        'porcentagem': len(
            booksByCategories[key]) * 100 / totalBooks
    }), keys
    )

    return list(countedBooks)


def writeCSVFile(filename, data):
    with open(filename, 'w', newline='') as file:
        fieldNames = ['categoria', 'porcentagem']
        writer = csv.DictWriter(
            file, fieldnames=fieldNames, extrasaction='ignore')

        writer.writeheader()
        writer.writerows(data)


def calcPercentage():
    data = readJsonFile()
    booksByCategory, totalBooks = groupBooks(data)

    quantityByCategories = booksPercentageByCategory(
        booksByCategory, totalBooks)

    writeCSVFile('booksPercentage.csv', quantityByCategories)


calcPercentage()
