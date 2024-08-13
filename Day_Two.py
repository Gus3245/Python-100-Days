#Python Primitive Data Types

#Data Types

#String

"Hello" #create String with ""

#pick a caracter

print("hello"[2])
#This is a Subscript (Go Print the Caracter L )
#Important, the Subscript always starts at 0

#This is not a number
"123"
print("123" + "34")
#This is concatenation

#Integer

123
#This is a number

print(123 + 123)
#print 246

123_234_345
#this is a number, 

#Float

3.144159

#Booleano

True
False

#Type Function
age = 123
type(age)
#Return <class int>

#converting to a string

new_age = str(age)
#return String "123"

#You can convert various types of variables
print(70 + float("170.5"))
print(str(70) + str(100))

#Mathematical Operations in Python

3 + 5 #Add
7 - 2 #Sub
8 * 2 #multiplication
6 / 3 #Return float Number -Division
6 // 3 #Return integer -Division
2 ** 2 #exponents

#Number Manipulation and F Strings in Python

print(round(8 / 3, 2))
#Return 2.67
#Round is a function to round numbers

#compound operators

result = 4 / 2
result /= 2

score = 0
score += 1

#F Strings


#Final Project
print("Welcome to the tip Calculator!")
bill = int(input("Wha was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
person = int(input("How many people to split the bill?"))
tip = tip / 100
final_anysen = (bill / person) * (1 + tip)

print(f"Each person should pay $ {final_anysen:.2f}")


