import turtle #import turtle that is a built-in drawing function

screen = turtle.Screen() #create a drawing screen
screen.bgcolor("blue") #bgcolor function set background for screen 
screen.title("Drawing Lines practice") #title function create a title

my_turtle = turtle.Turtle() #this creates a turtle
my_turtle.pensize(5) #pensize function for the size of the line
my_turtle.shape("circle") #the line will have a circle instead of the triangle
my_turtle.forward(100) #creates a line

#penup function 
#left function to change the direction of the line
#draw a 8-pointed star
for x in range(0, 8):
    my_turtle.forward(100)
    my_turtle.backward(100)
    my_turtle.left(45)


my_turtle.hideturtle() #to hide the turtle
turtle.done() #to tell that you are done with the program
