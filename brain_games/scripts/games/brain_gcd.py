#!/usr/bin/env python3

import prompt
from random import randint
from colorama import Fore, Style
from colorama import init
init(autoreset=True)


def main():
    print(Fore.CYAN + Style.BRIGHT + 'Welcome to the Brain Games!')
    brain_gcd()


def brain_gcd():
    print('Find the greatest common divisor of given numbers.')
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print()
    index = 1
    while index <= 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        print('Question: {} {}'.format(number_1, number_2))
        while number_1 != 0 and number_2 != 0:
            if number_1 > number_2:
                number_1 = number_1 % number_2
            else:
                number_2 = number_2 % number_1
        gcd = number_1 + number_2
        your_answer = prompt.string('Your answer: ')
        if your_answer == str(gcd):
            print(Fore.GREEN + 'Correct!')
            index += 1
        else:
            return print(
                Fore.RED +
                "'{}' is wrong answer ;(. Correct answer was '{}'."
                "\nLet\'s try again, {}!".format(your_answer, gcd, name))
    print(Fore.BLUE + Style.BRIGHT + 'Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
