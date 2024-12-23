# import turtle
# bello = turtle.Turtle()
#bello is an object
#turtle is a class
#Turtle is a method of the class turtle
#bello is an instance of the class turtle

# alternative :
# from turtle import Turtle
# bello = Turtle()

#car.spped
#car is a object and speed is an attribute
#this code says from this object(car) get this attribute(speed)


from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)# turtle moves by 100 paces
my_screen = Screen()
print(my_screen.canvheight)
#The Turtle object (timmy) is used to draw shapes or designs programmatically.
# The Screen object (my_screen) provides a canvas for the turtle's drawings 
# and allows interaction with properties like size, color, and events.
my_screen.exitonclick()# exits the code when we click on the screen or detects the click on the screen
# objectname.attribute
# objectname.methods


