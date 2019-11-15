#!/usr/bin/env python3

import prompt
from random import randint, choice
from colorama import Fore, Style
from colorama import init
init(autoreset=True)


def main():
    print(Fore.CYAN + Style.BRIGHT + 'Welcome to the Brain Games!')
    brain_calc()


def brain_calc():
    print('What is the result of the expression?')
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print()
    index = 1
    while index <= 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        operation = choice(['+', '-', '*'])
        if operation == '+':
            correct_answer = number_1 + number_2
        elif operation == '-':
            correct_answer = number_1 - number_2
        else:
            correct_answer = number_1 * number_2
        print('Question: {} {} {}'.format(number_1, operation, number_2))
        your_answer = prompt.string('Your answer: ')
        if your_answer == str(correct_answer):
            print(Fore.GREEN + 'Correct!')
            index += 1
        else:
            return print(
                Fore.RED +
                "'{}' is wrong answer ;(. Correct answer was '{}'."
                "\nLet\'s try again, {}!"
                .format(your_answer, correct_answer, name))
    print(Fore.BLUE + Style.BRIGHT + 'Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
