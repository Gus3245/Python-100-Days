#Namespaces: Local vs. Global Scope
from random import randint

 
EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess , answer, turns):
    """ Pass a guesse number who comaparet to the answer, return a turns - 1 or anything"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The  answer is {answer}")
    
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if difficulty == "easy":
       return EASY_LEVEL
    else:
       return HARD_LEVEL


def game():
    print("Welcome to the Nubmer Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)

    turns = set_difficulty()
    

    guess = 0
    while guess != answer:
        print(f"You Have {turns} attmpts remaining")
        guess = int(input("Make a Guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            print(f"The answer number is {answer}")
            break
        if guess != answer:
            print("Guess Again")
game()
