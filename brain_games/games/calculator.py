from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def get_conditions():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operation = choice(['+', '-', '*'])
    question = '{} {} {}'.format(number_1, operation, number_2)
    if operation == '+':
        correct_answer = str(number_1 + number_2)
    elif operation == '-':
        correct_answer = str(number_1 - number_2)
    else:
        correct_answer = str(number_1 * number_2)
    return (question, correct_answer)
