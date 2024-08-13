#Defining and Calling Python Functions

#Functions

#Functions are blocks of code that do something

print("Hello World!")
#this is a function 
len("Hello")
#tihs is a function

#() is the identifier for a function

#Make your function

def my_function(): #Create a function
    print("") #indention the function

#nothing happens if you don't call the function

my_function() #calling the function 

#bloc of codes

def my_function():
    if sky == "blue": #within the function
        print("Is blue") #within the function and if
    elif sky == "White": #within the function
        print("white") #within the function and elif
print("World") #out the function

#while loop

while Something_is_true:
    number = 6

#Exemple
numbers = 10
while  numbers > 0: #testing over and over again.
    print(numbers)
    numbers -= 1

#infinite loop
while 5 > 3:        #this is inifinite!!
    print("number")

#Reeborg's World Challenger

def turn_right():
    turn_left()
    turn_left()
    turn_left()
#46A1-D5B5
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    
    elif front_is_clear():
        move()
    else:
        move()

#This code only works here https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json