# The Basic Of All

#Print something in Terminal Using -- Print("") --
print("Hello World!")

#you can combine two String
print("Hello" + "World!")
#This is concatenation

#writing with line breaks
print("Hello \n World")

#Print Modifiers
#putting quotation marks around a word
print('She said : "Hello" and then left')

print("She said : 'Hello' and then left")

# escape backslash
print("She said : \"Hello\" and then left")

#print is a function in python

#Input something in Terminal Using -- input() --

input("A prompt for the user")
#tihs is print this String, and a location to type

#Concatenation print and input

print("Hello" + input("What is your name?"))
#anything that is typed will replace the input
#input = "type"

#comments are made using the # 
#This is a Comments.

#assigning a variable to the len function/method
numOfLetters = len("Angela")
print(numOfLetters)
#this function len, count the numbers of letters of your String.
#Resume The Code
print(len(input()))

#Variables
#In python, You don't need to specify the type of the variable
name = "James"
height = 1.45
year = 18
#You can print a variable
print(name)

#you can modify the value of the variable
name = "Angela"

#Ex Usign the len function
name = input("What is you name?")
length = len(name)
print(length)

#Final Project in Day One

print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)