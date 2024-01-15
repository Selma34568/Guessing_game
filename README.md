# Guessing_game
def play_qame(questions):
print("Welcome to our general culture game")

question_1 = input("What is the largest continent in the world?")
score = 0

if int(question_1) == "Asian continent":
    score = score + 5
    print("Great, user  answer is correct")
else:
    print("Unfortunately, user answer is wrong")

print("User score is -->",score)


question_2 = input ("How many countries are in the world?")
if int(question_2) == "250":
    score = score + 5
    print("Great, user  answer is correct")
else:
    print("Unfortunately, user answer is wrong")

print("User score is -->",score)
question_3 = input ("What is the smallest city in the world?")
if int(question_3) == "Vatikan":
    score = score + 5
    print("Great, user  answer is correct")
else:
    print("Unfortunately, user answer is wrong")

print("User score is -->",score)
question_4 = input("What is the capital of France?")
if int(question_4) == ("Paris"):
    score = score + 5
    print("Great, user  answer is correct")
else:
    print("Unfortunately, user answer is wrong")

print("User score is -->",score)
