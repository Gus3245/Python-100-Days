#Using the for loop with Python Lists

#For Loop

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

#print Apple, Peach , Pear
#indentetion is very important

#High Score Challenger

# Input a list of student scores

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

score = 0
for scores in range(0 ,len(student_scores)):
  if score > student_scores[scores]:
    score = score
  else:
    score = student_scores[scores]
print(f"The highest score in the class is: {score}")

#For loop not use Lists
soma = 0
for i in range(1, 101):
    soma += 1
print(soma)


for i in range(1, 101, 2): #step 2 in 2. 2, 4, 6...
    soma += 1
print(soma)

#Adding Even Numbers Challenger

target = int(input())
even_sum = 0

for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)

#FizzBuzz Challenger

target = 100

for number in range(1, target +1 , 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)


#Password Generator Project

import random
import string
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):               #choise aleatory letters
    password_list.append(random.choice(letters))    #

for char in range(1, nr_symbols + 1):               #choise aleatory symbols
    password_list.append(random.choice(symbols))    #

for char in range(1, nr_numbers + 1):               #choise aleatory numbers
    password_list.append(random.choice(numbers))    #
    
random.shuffle(password_list)   #Randomize the list

password = ""               #tranform the list in a simple String
for char in password_list:  #
   password += char         #

print(password)

