#Functions with Outputs
from art import logo

def format_name(f_name, l_name):
    """This function take a first and last name and format it to return the title case"""
    if f_name == "" or l_name == "":
        return 
    formated = f_name.title()
    formated_l = l_name.title()

    return f"{formated} {formated_l}"

formated_String = format_name("angela", "ANGELA")
print(formated_String)

#Docstrings

#Calculator Part 1: Combining Dictionaries and Functions

def add(n1, n2):
    return n1 + n2

def Subtract(n1, n2):
    return n1 - n2

def Multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

Calc = {
    "+": add,

    "-": Subtract,

    "*": Multiply,

    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What the first number?"))
    for symbol in Calc:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What the second number?"))
        calculation_function = Calc[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        operation_symbol = input("Pick another number: ")
        num3 = float(input("What the next number?: "))
        calculation_function = Calc[operation_symbol]
        second_ansqer = calculation_function(calculation_function(num1 , num2), num3)

        if input(f"Type 'y' to continue calculating wirh {answer}:") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()