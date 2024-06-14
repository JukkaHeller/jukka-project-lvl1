from random import randint

QUESTION = 'What number is missing in the progression?'

progression_min_length = 5
progression_max_length = 10

def game():
progression_start = randint(1, 100)
step = randint(1, 10)
progression_length = randint(5, 10)
blank_index = randint(0, progression_length)
progression = [progression_start+step for x in range(progression_length)]
    question = f'{number_1} {number_2}'

    while 0 not in (number_1, number_2):
        if number_1 > number_2:
            number_1, number_2 = number_1 % number_2, number_2
        elif number_1 < number_2:
            number_1, number_2 = number_2 % number_1, number_1
        else:
            correct_answer = number_1
    correct_answer = str(max(number_1, number_2))
    return question, correct_answer
