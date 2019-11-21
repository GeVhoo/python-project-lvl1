from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_conditions():
    number = randint(2, 100)
    question = number
    d = 2
    while number % d != 0:
        d += 1
    if d != number:
        correct_answer = 'no'
    if d == number:
        correct_answer = 'yes'
    return (question, correct_answer)
