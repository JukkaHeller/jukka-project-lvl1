from random import randint

QUESTION = 'Find the greatest common divisor of given numbers.'


def game():
    number_1 = randint(1, 50)
    number_2 = randint(1, 50)
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
