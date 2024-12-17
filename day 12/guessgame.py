# guess the number game

from random import randint
easy_level = 10
hard_level = 5

turns = 0
def check_answer(guess, answer, turns):

    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it!. The answer is {answer}")
       

def set_difficulty():
    level = input("Choose a difficulty. Type 'E' for easy or 'H' for hard: ")
    if level.upper() == "E":
       return easy_level
    elif level.upper() == "H":
       return hard_level

def game():   
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    turns = set_difficulty()
    

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess == answer:
            print(f"You got it!. The answer is {answer}")
game()