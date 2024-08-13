#How to use OOP: Classes and Objects

"""
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
for steps in range(20):
    for c in ('blue', 'red', 'green'):
        timmy.color(c)
        timmy.forward(steps)
        timmy.right(30)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
"""

from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"

table.add_column("Pokemon Name", ["Pikachu","Snowler","Chamander", "Bem-Te-Vi"])
table.add_column("Life Time", [5 ,6 ,10 ,30])
print(table)
