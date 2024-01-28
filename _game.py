import random

def play_game():
    print("Welcome to our general culture game")


    user_name = input("What's your name? ")

    game_theme = input("Choose a game theme (e.g., history, geography, science , all themes): ")

    score = 0
    lives = 3

    if game_theme.lower() == 'geography':
        questions_answer = [
            {'question': 'Which country is in the Asian continent?',
             'options': ['Madagascar', 'Peru', 'Singapore'],
             'answer': 'Singapore'},
            {'question': 'What is the largest continent in the world?',
             'options': ['Europe', 'Asian continent', 'Africa', 'Antarctica'],
             'answer': 'Asian continent'},
            {'question': 'How many countries are in the world?',
             'options': ['200', '250', '275', '100'],
             'answer': '250'}
        ]

    elif game_theme.lower() == 'history':
        questions_answer = [
            {'question': 'In what year did the first world war occur?',
             'options': ['1915', '1936', '1914', '1923'],
             'answer': '1914'},
            {'question': 'Who is the author of the novel "Crime and Punishment?',
             'options': ['Leo Tolstoy', 'Fyodor Dostoyevsky', 'Anton Chekhov', 'Ivan Turgenev'],
             'answer': 'Fyodor Dostoyevsky'},
            {'question': 'Who set foot on the moon for the first time?',
             'options': ['Elon Musk', 'Neil Armstrong', 'Yuri Gagarin', 'Louis Armstrong'],
             'answer': 'Neil Armstrong'}
        ]
    elif game_theme.lower() == 'science':
        questions_answer = [
            {'question': 'What is the chemical symbol for water?',
             'options': ['H2O', 'CO2', 'O2', 'N2'],
             'answer': 'H2O'},
            {'question': 'What are the first few decimal places of pi?',
             'options': ['3.1415926535...', '3.1515926535...', '3.1615926535...', '3.1715926535...'],
             'answer': '3.1415926535...'},
            {'question': 'What is the largest planet in the Solar System?',
             'options': ['Jupiter', 'Uranus', 'Neptune', 'Mercury'],
             'answer': 'Jupiter'}
        ]
    elif game_theme.lower() == 'all themes':
        questions_answer = [
            {'question': 'Which country is in the Asian continent?',
             'options': ['Madagascar', 'Peru', 'Singapore'],
             'answer': 'Singapore'},
            {'question': 'What is the largest continent in the world?',
             'options': ['Europe', 'Asian continent', 'Africa', 'Antarctica'],
             'answer': 'Asian continent'},
            {'question': 'How many countries are in the world?',
             'options': ['200', '250', '275', '100'],
             'answer': '250'},
            {'question': 'In what year did the first world war occur?',
             'options': ['1915', '1936', '1914', '1923'],
             'answer': '1914'},
            {'question': 'Who is the author of the novel "Crime and Punishment?',
             'options': ['Leo Tolstoy', 'Fyodor Dostoyevsky', 'Anton Chekhov', 'Ivan Turgenev'],
             'answer': 'Fyodor Dostoyevsky'},
            {'question': 'Who set foot on the moon for the first time?',
             'options': ['Elon Musk', 'Neil Armstrong', 'Yuri Gagarin', 'Louis Armstrong'],
             'answer': 'Neil Armstrong'},
            {'question': 'What is the chemical symbol for water?',
             'options': ['H2O', 'CO2', 'O2', 'N2'],
             'answer': 'H2O'},
            {'question': 'What are the first few decimal places of pi?',
             'options': ['3.1415926535...', '3.1515926535...', '3.1615926535...', '3.1715926535...'],
             'answer': '3.1415926535...'},
            {'question': 'What is the largest planet in the Solar System?',
             'options': ['Jupiter', 'Uranus', 'Neptune', 'Mercury'],
             'answer': 'Jupiter'}

        ]
    else:
        print("Invalid theme. Exiting the game.")
        return

    random.shuffle(questions_answer)

    for question in questions_answer:
        user_input = input(f"{question['question']} ({', '.join(question['options'])}): ").lower()

        if user_input == question['answer'].lower():
            score += 5
            print("Great, your answer is correct!")
        else:
            print('Unfortunately, your answer is wrong')
            lives -= 1
            print(f'You have {lives} lives remaining.\n')

        if lives == 0:
            print(f"Game over, {user_name}! Your final score is: {score}")
            break
        elif lives > 0:
            print(f'Your score is: {score}')

    total_score = score * 5  # 5 points for each correct answer
    print(f'Thanks for playing, {user_name}!')
    print(f'Your total score is: {total_score}')

play_game()

