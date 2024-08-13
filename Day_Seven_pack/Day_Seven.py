#Challenge 1 - Picking a Random Words and Checking Answers

import random
from hangman_art import logo, stages
from hangman_words import word_list



list_random = random.choice(word_list)
word_lenght = len(list_random)

display = []
for _ in range(len(list_random)):
        display += "_"

end_of_game = False
lives = 6

print(logo)


while not end_of_game:

    Guess = (input("Digite anything letter ")).lower()

    

    if Guess in display:
         print(f"You've already guessed this letter {Guess}")
   

    for position in range(0, word_lenght):
        letters = list_random[position]

        if letters == Guess:  
            display[position] = letters
            if Guess in list_random:
                print(f"you typed the letter {Guess}, right letter")
        
 
    if "_" not in display:
        end_of_game = True
        print("You Win")

    if Guess not in list_random:
        lives -= 1
        print(stages[lives])
        print(f"The Letter {Guess}, is not in the Word")
        
        if lives == 0:
            end_of_game = True
            print("Game Over")
            print(f"The Word is {list_random}")
    

    

    print(f"{''.join(display)}")

#Challenge 2 - Replacing Blanks with Guesses

#Challenge 3 - Checking if the Player has Won

#Challenge 4 - Keeping Track of the Player's Lives


