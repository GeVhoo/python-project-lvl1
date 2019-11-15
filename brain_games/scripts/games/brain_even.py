#!/usr/bin/env python3

import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    brain_even()


def brain_even():
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print()
    index = 1
    while index <= 3:
        random_number = randint(1, 100)
        print('Question: {}'.format(str(random_number)))
        your_answer = prompt.string('Your answer: ')
        if (random_number % 2) == 0 and your_answer == 'yes':
            print('Correct!')
            index += 1
        elif (random_number % 2) != 0 and your_answer == 'no':
            print('Correct!')
            index += 1
        else:
            if (random_number % 2) == 0:
                return print(
                    "'{}' is wrong answer ;(. Correct answer was '{}'."
                    "\nLet\'s try again, {}!".format(your_answer, 'yes', name))
            return print(
                    "'{}' is wrong answer ;(. Correct answer was '{}'."
                    "\nLet\'s try again, {}!".format(your_answer, 'no', name))
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
