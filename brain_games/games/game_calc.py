import random
from random import randint
import operator

QUESTION = 'What is the result of the expression?'


operator_functions = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

operators = ["+", "-", "*"]

picked_operator = random.choice(operators)


def game():
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    question = f'{number_1} {picked_operator} {number_2}'
    correct_answer = str(operator_functions[picked_operator]
                         (number_1, number_2))
    return question, correct_answer
