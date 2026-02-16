import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Matching the dark background in your photo

# Set up the turtle
t = turtle.Turtle()
t.speed(0.7)               # Fastest speed
t.color("white")         # Set the line color to white
t.pensize(2)

def draw_petal():
    """Draws a single pointed petal using two arcs."""
    for _ in range(2):
        t.circle(100, 90)    # Draw a 90-degree arc with radius 100
        t.left(90)           # Turn to create the sharp point

# Draw the full flower pattern
# We repeat the petal many times, rotating slightly each time
for i in range(36):
    draw_petal()
    t.left(10)               # Rotate 10 degrees for the next petal

# Hide the turtle and keep window open
t.hideturtle()
screen.exitonclick()