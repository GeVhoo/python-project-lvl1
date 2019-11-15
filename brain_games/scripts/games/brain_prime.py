#!/usr/bin/env python3

import prompt
from random import randint, choice
from colorama import Fore, Style
from colorama import init
init(autoreset=True)


def main():
    print(Fore.CYAN + Style.BRIGHT + 'Welcome to the Brain Games!')
    brain_prime()


def brain_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print()
    index = 1
    while index <= 3:
        number = randint(2, 100)
        d = 2
        while number % d != 0:
            d += 1
        if d != number:
            correct_answer = 'no'
        if d == number:
            correct_answer = 'yes'
        print('Question: {}'.format(number))
        your_answer = prompt.string('Your answer: ')
        if your_answer == correct_answer:
            print(Fore.GREEN + 'Correct!')
            index += 1
        else:
            return print(Fore.RED +
                    "'{}' is wrong answer ;(. Correct answer was '{}'."
                    "\nLet\'s try again, {}!".format(your_answer, correct_answer, name))
    print(Fore.BLUE + Style.BRIGHT + 'Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
