from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    question = randint(2, 100)
    divider_list = [x for x in range(2, question)
                    if question % x == 0]
    if len(divider_list) > 0:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return question, correct_answer
