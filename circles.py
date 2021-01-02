import turtle #import turtle that is a built-in drawing function

screen = turtle.Screen() #create a drawing screen
screen.bgcolor("blue") #bgcolor function set background for screen 
screen.title("Drawing Lines practice") #title function create a title

my_turtle = turtle.Turtle() #this creates a turtle
my_turtle.pensize(5) #pensize function for the size of the line
my_turtle.shape("circle")
my_turtle.color("red")
my_turtle.fillcolor("red")
my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.end_fill()

my_turtle.hideturtle()
turtle.done()
