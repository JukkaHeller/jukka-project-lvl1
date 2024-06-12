import prompt

ANSWERS_COUNTER = 3  # how many times to ask


def game_engine(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game_question = game.QUESTION
    print(game_question)

    for _ in range(ANSWERS_COUNTER):
        question, correct_answer = game.game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f'Correct answer was \'{correct_answer}\'.'
                  f'Let\'s try again {name}')
            break
    else:
        print(f'Congratulations, {name}!')
