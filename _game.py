import random

class GeneralCultureGame:
    def __init__(self):
        print("Welcome to our general culture game")
        self.user_name = input("What's your name? ")
        self.game_theme = input("Choose a game theme (e.g., history, geography, science, all themes): ")
        self.score = 0
        self.lives = 3

        self.questions_answer = []

        self.setup_questions()

    def setup_questions(self):
        if self.game_theme.lower() == 'geography':
            self.questions_answer = [
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
        elif self.game_theme.lower() == 'history':
          self.questions_answer = [
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
        elif self.game_theme.lower() == 'science':
          self.questions_answer = [
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
        

        elif self.game_theme.lower() == 'all themes':
            self.questions_answer = [
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

        random.shuffle(self.questions_answer)

    def play_game(self):
        for question in self.questions_answer:
            user_input = input(f"{question['question']} ({', '.join(question['options'])}): ").lower()

            if user_input == question['answer'].lower():
                self.score += 5
                print("Great, your answer is correct!")
            else:
                print('Unfortunately, your answer is wrong')
                self.lives -= 1
                print(f'You have {self.lives} lives remaining.\n')

            if self.lives == 0:
                print(f"Game over, {self.user_name}! Your final score is: {self.score}")
                break
            elif self.lives > 0:
                print(f'Your score is: {self.score}')

        total_score = self.score * 5  
        print(f'Thanks for playing, {self.user_name}!')
        print(f'Your total score is: {total_score}')


game_instance = GeneralCultureGame()
game_instance.play_game()
        
