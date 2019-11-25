from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def get_conditions():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    symbol, operation = choice([('+', add), ('-', sub), ('*', mul)])
    question = '{} {} {}'.format(number1, symbol, number2)
    correct_answer = str(operation(number1, number2))
    return (question, correct_answer)
