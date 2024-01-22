def play_qame(questions):
    print("Welcome to our general culture game")

score = 0
lives = 3
guestions_answer = [
    {'guestion': 'What is the largest continent in the world?',
     'options': ['Europe', 'Asian continent', 'Africa', 'Antarctica']},

]
guestions_answers = [
    {'guestion': 'What is the largest continent in the world?',
     'user_answer':'Asian continent'}
]

for guestion in guestions_answers:
     if 'answer_input' == 'q[answer]'.lower():
        score += score +5
        print("Great, user  answer is correct")
     else:
        print('Unfortunately, user answer is wrong')
        lives -= 1
        print(f'You have {lives} lives remaining.\n')

     if lives == 0:
        print('Game over! Your score is : ', score)
        break


questions_answer = [
    {'question': 'How many countries are in the world?','answer':0,
     'options': ['200', '250', '275', '100']}

]
guestions_answers = [
    {'question':'How many countries are in the world?',
     'user_answer': '250'}
]

for guestion in guestions_answers:
     if 'answer_input' == 'q[answer]'.lower():
        score += score +5
        print("Great, user  answer is correct")
     else:
        print('Unfortunately, user answer is wrong')
        lives -= 1
        print('Game over! Your score is : ', score)
        break



guestions_answer = [
    {'guestion':'What is the smallest country in the world?','answer':0,
     'options':['Monako','Vatikan','Nauru','Tuvalu']}

]
guestions_answers = [
    {'guestion': 'What is the smallest country in the world?',
     'user_answer': 'Vatikan'}
]

for guestion in guestions_answers:
    if 'answer_input' == 'q[answer]'.lower():
        score += score + 5
        print('Great, user answer is correct')
    else:
        print('Unfortunately, user answer is wrong')
        lives -= 1
        print('Game over! Your score is : ', score)
        break



guestions_answer = [
    {'question': 'What is the capital city England?',
     'answer': ['Paris','London','Warsaw','Berlin']}

]
guestions_answers = [
    {'question': 'What is the capital city England?',
     'user_answer': 'London'}

]

for guestion in guestions_answers:
    if 'answer_input' == 'g[answer]'.lower():
        score += score + 5
        print('Great, user answer is correct')
    else:
        print('Unfortunately user answer is wrong')
        lives -= 1
        print('Game over! Your score is :',score)
        break


print('User score is Warsaw',score)
