import turtle

# Function to draw the Egyptian flag
def draw_flag():
    # Create a screen for the turtle graphics, set the width and height
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  # Setting screen size to 800x600 pixels
    screen.bgcolor("white")  # Set background color to white
    
    # Create a turtle to draw the flag
    pen = turtle.Turtle()
    pen.speed(0)  # Set the drawing speed to the fastest

    # Drawing the red stripe (top part of the flag)
    pen.penup()  # Lift the pen so it doesn't draw as it moves to the starting position
    pen.goto(-150, 50)  # Move the turtle to the starting position (centered on the screen)
    pen.pendown()  # Put the pen down to start drawing
    pen.color("red")  # Set the pen color to red for the red stripe
    pen.begin_fill()  # Start filling the shape with red color
    for _ in range(2):
        pen.forward(300)  # Draw the length of the rectangle (width of the flag)
        pen.right(90)  # Turn the turtle 90 degrees to the right
        pen.forward(50)  # Draw the height of the rectangle (height of the flag stripes)
        pen.right(90)  # Turn the turtle 90 degrees to the right again
    pen.end_fill()  # Complete the filling of the red rectangle

    # Drawing the white stripe (middle part of the flag)
    pen.penup()
    pen.goto(-150, 0)  # Move the turtle to the position of the white stripe
    pen.pendown()  # Put the pen down to start drawing
    pen.color("white")  # Set the pen color to white for the white stripe
    pen.begin_fill()  # Start filling the shape with white color
    for _ in range(2):
        pen.forward(300)  # Draw the width of the rectangle
        pen.right(90)
        pen.forward(50)  # Draw the height of the rectangle
        pen.right(90)
    pen.end_fill()  # Complete the filling of the white rectangle

    # Drawing the black stripe (bottom part of the flag)
    pen.penup()
    pen.goto(-150, -50)  # Move the turtle to the position of the black stripe
    pen.pendown()
    pen.color("black")  # Set the pen color to black for the black stripe
    pen.begin_fill()  # Start filling the shape with black color
    for _ in range(2):
        pen.forward(300)  # Draw the width of the rectangle
        pen.right(90)
        pen.forward(50)  # Draw the height of the rectangle
        pen.right(90)
    pen.end_fill()  # Complete the filling of the black rectangle

    # Add the eagle image to the flag (on the white stripe)
    add_eagle(screen)

    # Hide the turtle after drawing
    pen.hideturtle()
    screen.mainloop()  # Keep the screen open until manually closed

# Function to add the eagle image to the center of the flag
def add_eagle(screen):
    # Register the eagle image (must be in the same directory as the script)
    screen.register_shape("eagle_small.gif")  # Register the small eagle image
    eagle = turtle.Turtle()  # Create a new turtle to represent the eagle
    eagle.shape("eagle_small.gif")  # Set the shape of the turtle to the eagle image
    eagle.penup()  # Lift the pen so the turtle doesn't draw lines
    eagle.goto(0, -25)  # Position the eagle at the center of the white stripe (adjust position)
    
# Call the function to draw the flag
draw_flag()
