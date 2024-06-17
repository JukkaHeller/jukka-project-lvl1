from random import randint

QUESTION = 'What number is missing in the progression?'

progression_min_length = 5
progression_max_length = 10


def game():
    progression_start = randint(1, 100)
    step = randint(1, 10)
    progression_length = randint(progression_min_length,
                                 progression_max_length)
    blank_index = randint(0, progression_length - 1)
    progression = [progression_start + x * step for x
                   in range(progression_length)]
    missing_number = progression[blank_index]
    progression[blank_index] = '..'
    question = ' '.join((str(x) for x in progression))
    correct_answer = str(missing_number)
    return question, correct_answer
