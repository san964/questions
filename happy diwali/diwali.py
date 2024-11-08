import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Happy Diwali!")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create a turtle for fireworks
firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)

# Create a turtle for writing text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.color("yellow")
text_turtle.penup()


# Function to draw a firework explosion
def draw_firework(x, y):
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    firework.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange", "white"]))

    for _ in range(20):  # Create 20 lines for the explosion
        angle = random.randint(0, 360)
        distance = random.randint(50, 100)
        firework.setheading(angle)
        firework.forward(distance)
        firework.backward(distance)


# Display "Happy Diwali!" text
def display_text():
    text_turtle.goto(0, -200)
    text_turtle.write("Happy Diwali!", align="center", font=("Arial", 36, "bold"))


# Show fireworks animation
def show_fireworks():
    for _ in range(10):  # Number of fireworks to display
        x = random.randint(-300, 300)
        y = random.randint(-100, 200)
        draw_firework(x, y)
        time.sleep(0.5)  # Delay between each firework


# Run the display
display_text()
show_fireworks()

# Hide turtles and keep the window open
firework.hideturtle()
turtle.done()
