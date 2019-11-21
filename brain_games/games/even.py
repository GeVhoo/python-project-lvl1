from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_conditions():
    random_number = randint(1, 100)
    question = random_number
    if (random_number % 2) == 0:
        correct_answer = 'yes'
    elif (random_number % 2) != 0:
        correct_answer = 'no'
    return (question, correct_answer)
