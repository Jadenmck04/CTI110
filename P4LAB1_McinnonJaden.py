import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create the turtle
t = turtle.Turtle()
t.color("brown")
t.pensize(3)
t.speed(3)

# Draw the square (house) using a while loop
count = 0
while count < 4:
    t.forward(150)
    t.left(90)
    count += 1

# Move to the roof starting point
t.left(90)
t.forward(150)
t.right(90)

# Draw the triangle (roof) using a for loop
t.color("red")
for i in range(3):
    t.forward(150)
    t.left(120)

# Draw the door
t.penup()
t.goto(55, 0)
t.setheading(90)
t.pendown()
t.color("darkgreen")

for i in range(2):
    t.forward(75)
    t.right(90)
    t.forward(40)
    t.right(90)

# Draw left window
t.penup()
t.goto(20, 80)
t.setheading(0)
t.pendown()
t.color("yellow")

for i in range(4):
    t.forward(30)
    t.right(90)

# Draw right window
t.penup()
t.goto(100, 80)
t.setheading(0)
t.pendown()

for i in range(4):
    t.forward(30)
    t.right(90)

# Draw the sun
t.penup()
t.goto(-180, 180)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(30)
t.end_fill()

# Finish
t.hideturtle()
turtle.done()