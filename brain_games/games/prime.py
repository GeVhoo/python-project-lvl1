from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    d = 3
    while d <= sqrt(number) and number % d != 0:
        d += 2
    return d > sqrt(number)


def get_conditions():
    number = randint(2, 100)
    question = number
    correct_answer = 'yes' if is_prime(number) else 'no'
    return (question, correct_answer)
