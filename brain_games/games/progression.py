from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'


def get_conditions():
    step = randint(1, 10)
    n1 = randint(1, 10)
    n2 = n1 + step
    n3 = n2 + step
    n4 = n3 + step
    n5 = n4 + step
    n6 = n5 + step
    n7 = n6 + step
    n8 = n7 + step
    n9 = n8 + step
    n10 = n9 + step
    list_n = (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)
    random_n = choice(list_n)
    correct_answer = str(random_n)
    mask = []
    for item in list_n:
        if item == random_n:
            mask.append('..')
        elif item != random_n:
            mask.append(item)
    mask = str(mask)
    list_char = "[],'"
    for char in list_char:
        mask = mask.replace(char, '')
    question = mask
    return (question, correct_answer)
