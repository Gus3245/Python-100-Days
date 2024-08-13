#Random Module

import random
#import random library of python.

random_integer = random.randint(1 , 10)
print(random_integer)
#print a number 

random_float = random.random() #function generator number 0.0000 -> 0.9999
print(random_float)

#Understanding the Offset and Appending Items to Lists

#Lists

fruits = ["aplee", "Orange"]
number = [1 ,2 ,3 ,4 ,5]

state1 = "Ceará"
state2 = "Rio de janeiro"
brasil = [state1, state2]
print(brasil[0]) 

#print the index 0 for the list
#all lists starter with 0

print(brasil[-1]) #starter the list for the end
#print state2

#Change valors in a list
brasil[0] = "Bahia"

brasil.append("Paraiba") #add a new item in list.
brasil.extend(["São paulo", "Acre"]) #add a new list in a list.

list_of_list = [brasil, fruits] #two list on a one

#Test

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]


print("Hiding your treasure! X marks the spot.")
position = input()

letter = position[0].lower()
number = position[1]

abc = ["a" , "b" , "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")


#Day 4 Project: Rock Paper Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")




