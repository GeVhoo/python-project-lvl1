from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_conditions():
    number1 = randint(1, 10)
    step = randint(1, 10)
    index = 0
    random_index = randint(1, 8)
    result = ''
    while index < 10:
        next_number = str(number1 + (index * step))
        if result:
            result += ' '
        if random_index == index:
            result += '..'
            correct_answer = next_number
        else:
            result += next_number
        index += 1
    question = result
    return (question, correct_answer)
