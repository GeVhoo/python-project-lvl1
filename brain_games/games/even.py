from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return not (number % 2)


def get_conditions():
    number = randint(1, 100)
    question = number
    correct_answer = 'yes' if is_even(number) else 'no'
    return (question, correct_answer)
