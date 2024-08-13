import turtle as t
import random
import colorsys

t = t.Turtle()
"""
t2 = Turtle()
t2.color("red")

for ang in range(0, 4):
    t.forward(100)
    t.left(90)
    t2.left(90)
    t2.forward(100)

for ang in range(0 , 10):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)

"""

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", 
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
t.screen.bgcolor("Black")

"""
def draw_shape(sides):

    angle = 360 / sides
    random_color = random.choice(colours)
    for ang in range(sides):
        t.color(random_color)
        t.forward(100)
        t.right(angle)
    
    sides += 1

for shape_Side_n in range(3, 11):
    draw_shape(shape_Side_n)
"""

"""
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r ,g, b)
    return random_color

Position = [0 , 90 , 180 , 270]
def Forward_turtle(color):
    t.pensize(5)
    t.speed(10)
    for ang in range(100):
        t.color(random_color())
        t.forward(30)
        t.setheading(random.choice(Position))
        
Forward_turtle()

"""
h = 0
n = 70
t.speed(0)

for _ in range(360):
    c = colorsys.hsv_to_rgb(h ,1 , 0.8)
    h += 1/n
    t.color(c)
    
    
    for i in range(2):
        t.left(2)
        t.circle(100)
        



screen = t.Screen()
screen.exitonclick()