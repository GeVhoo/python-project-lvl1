from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    while number1 and number2:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return str(number1 + number2)


def get_conditions():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = '{} {}'.format(number1, number2)
    correct_answer = gcd(number1, number2)
    return (question, correct_answer)
