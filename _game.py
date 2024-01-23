


def play_qame(questions):
    print("Welcome to our general culture game")

score = 0
lives = 3

questions_answer = [
    {'question': 'What is the largest continent in the world?',
     'options': ['Europe', 'Asian continent', 'Africa', 'Antarctica'],
     'answer': 'Asian continent'}
]

for question in questions_answer: 
    user_input = input(f"{question['question']} ({', '.join(question['options'])}): ").lower()

    if user_input == question['answer'].lower():
        score += 5
        print("Great, user answer is correct")
    else:
        print('Unfortunately, user answer is wrong')
        lives -= 1
        print(f'You have {lives} lives remaining.\n')

    if lives == 0:
        print('Game over! Your score is:', score)
        break


score = 0
lives = 3

questions_answer = [
    {'question': 'How many countries are in the world?',
     'options': ['200', '250', '275', '100'],
     'answer': '250'}
]

for question in questions_answer:
    user_input = input(f"{question['question']} ({', '.join(question['options'])}): ").lower()

    if user_input == question['answer'].lower():
        score += 5
        print("Great, user answer is correct")
    else:
        print('Unfortunately, user answer is wrong')
        lives -= 1
        print(f'You have {lives} lives remaining.\n')

    if lives == 0:
        print('Game over! Your score is:', score)
        break



score = 0
lives = 3

questions_answer = [
    {'question': 'What is the smallest country in the world??',
     'options': ['Monako','Vatikan','Nauru','Tuvalu'],
     'answer': 'Vatikan'}
]

for question in questions_answer:
    user_input = input(f"{question['question']} ({', '.join(question['options'])}): ").lower()

    if user_input == question['answer'].lower():
        score += 5
        print("Great, user answer is correct")
    else:
        print('Unfortunately, user answer is wrong')
        lives -= 1
        print(f'You have {lives} lives remaining.\n')

    if lives == 0:
        print('Game over! Your score is:', score)
        break



score = 0
lives = 3

questions_answer = [
    {'question': 'What is the capital city England?',
     'options': ['Paris','London','Warsaw','Berlin'],
     'answer': 'London'}
]

for question in questions_answer:
    user_input = input(f"{question['question']} ({', '.join(question['options'])}): ").lower()

    if user_input == question['answer'].lower():
        score += 5
        print("Great, user answer is correct")
    else:
        print('Unfortunately, user answer is wrong')
        lives -= 1
        print(f'You have {lives} lives remaining.\n')

    if lives == 0:
        print('Game over! Your score is:', score)
        break




questions_answer = [
    {'question': 'What is the largest continent in the world?',
     'options': ['Europe', 'Asia', 'Africa', 'Antarctica'],
     'answer': 'Asia'},

    {'question': 'How many countries are in the world?',
     'options': ['200', '250', '275', '100'],
     'answer': '250'},

    {'question': 'What is the smallest country in the world?',
     'options': ['Monaco', 'Vatican', 'Nauru', 'Tuvalu'],
     'answer': 'Vatikan'},

    {'question': 'What is the capital city of England?',
     'options': ['Paris', 'London', 'Warsaw', 'Berlin'],
     'answer': 'London'},

]

