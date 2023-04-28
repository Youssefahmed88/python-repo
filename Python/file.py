import turtle

# Create a turtle to control
t = turtle.Turtle()

# Set up the turtle screen to flip 90 degrees
turtle.screensize(600, 600)
turtle.setworldcoordinates(600, 0, 0, 600)

# Set starting position
x, y = 200, 200

# Define colors for squares
colors = ["blue", "red", "yellow", "green"]

# Draw largest square (blue)
t.penup()
t.goto(60, 300)
t.pendown()
t.color(colors[0])
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()

# Draw second largest square (red)
x -= 50
y -= 50
t.penup()
t.goto(110, 250)
t.pendown()
t.color(colors[1])
t.begin_fill()
for i in range(4):
    t.forward(150)
    t.right(90)
t.end_fill()

# Draw third largest square (yellow)
x -= 50
y -= 50
t.penup()
t.goto(180, 190)
t.pendown()
t.color(colors[2])
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

# Draw smallest square (green)
x -= 20
y -= 60
t.penup()
t.goto(250, 120)
t.pendown()
t.color(colors[3])
t.begin_fill()
for i in range(4):
    t.forward(40)
    t.right(90)
t.end_fill()

# Hide turtle after drawing is complete
t.hideturtle()

# Keep the turtle window open until it is clicked
turtle.done()
