import random

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


scrambledWordGame(['Janaina', 'Comer', 'Vacina'])
