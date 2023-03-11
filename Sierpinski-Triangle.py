import turtle
import random

amount = int(input("How many iterations would you like? "))

WIDTH, HEIGHT = 1000, 1000

win = turtle.Screen()
win.setup(WIDTH, HEIGHT)
win.bgcolor("black")
win.title('Sierpinski Triangle')

t = turtle.Turtle()
t.hideturtle()
t.speed('fastest')
t.shape("square")
t.shapesize(0.05, 0.05)
t.up()

t2 = turtle.Turtle()
t2.hideturtle()
t2.color('white')
t2.penup()
t2.setpos(300, 400)

p1 = (-250, -250)
p2 = (0, 250)
p3 = (250, -250)

points = [p1, p2, p3]

mid_point = (50, 50)

colours = ['red', 'green', 'blue']

# set stamp counter to 0.
t2.write(0, font=('', 50, 'normal'))

for i in range(0, amount):
    # sierpinski triangle algorithm
    rand_point = points[random.randint(0, 2)]
    mid_point  = ((rand_point[0] + mid_point[0]) / 2, 
                  (rand_point[1] + mid_point[1]) / 2)
    t.goto(mid_point)
    t.color(colours[random.randint(0, 2)])
    t.stamp() 
    # total stamp counter.
    if t.pos() == mid_point:
        t2.undo()
        t2.write(i+1, font=('', 50, 'normal'))  

turtle.done()
