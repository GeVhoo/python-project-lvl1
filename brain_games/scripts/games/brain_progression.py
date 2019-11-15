#!/usr/bin/env python3

import prompt
from random import randint, choice
from colorama import Fore, Style
from colorama import init
init(autoreset=True)


def main():
    print(Fore.CYAN + Style.BRIGHT + 'Welcome to the Brain Games!')
    brain_progression()


def brain_progression():
    print('What number is missing in the progression?')
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print()
    index = 1
    while index <= 3:
        step = randint(1, 10)
        n1 = randint(1, 10)
        n2 = n1 + step
        n3 = n2 + step
        n4 = n3 + step
        n5 = n4 + step
        n6 = n5 + step
        n7 = n6 + step
        n8 = n7 + step
        n9 = n8 + step
        n10 = n9 + step
        list_n = (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)
        random_n = choice(list_n)
        mask = []
        for item in list_n:
            if item == random_n:
                mask.append('..')
            elif item != random_n:
                mask.append(item)
        mask = str(mask)
        list_char = "[],'"
        for char in list_char:
            mask = mask.replace(char, '')
        print('Question: {}'.format(mask))
        your_answer = prompt.string('Your answer: ')
        if your_answer == str(random_n):
            print(Fore.GREEN + 'Correct!')
            index += 1
        else:
            return print(
                Fore.RED +
                "'{}' is wrong answer ;(. Correct answer was '{}'."
                "\nLet\'s try again, {}!".format(your_answer, random_n, name))
    print(Fore.BLUE + Style.BRIGHT + 'Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
