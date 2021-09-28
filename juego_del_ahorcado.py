import os
import random
import unidecode
import time

banners = {
    'ahorcado':
        "    _    _                             _\n"\
        "   / \  | |__   ___  _ __ ___ __ _  __| | ___\n"\
        "  / _ \ | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \ \n"\
        " / ___ \| | | | (_) | | | (_| (_| | (_| | (_) |\n"\
        "/_/   \_\_| |_|\___/|_|  \___\__,_|\__,_|\___/\n"\
        "            Por: Missael Barco 😜   ",
    'felicidades':
        " _____ _____ _     ___ ____ ___ ____    _    ____  _____ ____\n"\
        "|  ___| ____| |   |_ _/ ___|_ _|  _ \  / \  |  _ \| ____/ ___|\n"\
        "| |_  |  _| | |    | | |    | || | | |/ _ \ | | | |  _| \___ \ \n"\
        "|  _| | |___| |___ | | |___ | || |_| / ___ \| |_| | |___ ___) |\n"\
        "|_|   |_____|_____|___\____|___|____/_/   \_\____/|_____|____/\n"
}

def equal(word, word_game):
    """Compare if two strings are equal regardless of uppercases and accents"""
    word = unidecode.unidecode(word.lower())
    word_game = unidecode.unidecode(word_game.lower())

    return word == word_game

def play(letter, word, word_game):
    """Check if letter is in the word and return current game state"""
    word = unidecode.unidecode(word.lower())
    word_game = list(word_game)

    for i, word_letter in enumerate(word):
        if word_letter == letter:
            word_game[i] = letter

    return ''.join(word_game)

def main():

    with open('./archivos/data.txt', 'r') as f:
        word = random.choice(f.read().splitlines())

    word_game = ''.join(['_' for i in range(len(word))])

    while not equal(word, word_game):
        try:
            os.system('clear')
            print(banners['ahorcado'])
            print(word_game)
            letter = input('Ingresa una letra y presiona enter😁: ')

            if letter.isdigit():
                raise Exception('Las palabras no tienen números 😜')
            if len(letter) > 1:
                raise Exception('Debes introducir una sola letra 🙄')
            if len(letter) == 0:
                raise Exception('Escribe algo!😫')

            word_game = play(letter, word, word_game)

        except Exception as ve:
            print(ve)
            time.sleep(1)

    os.system('clear')
    print(banners['felicidades'], '\t ✨💕 Ganaste con la palabra: ', word, '✨💕')


if __name__=='__main__':
    main()