# functions with multiple inputs
# eg:
# def my_function(something, something_else):
#dothis with something and something_else
#then do this
# then do this
def greet_name(name, age): # taks two functions 
    print(f"Hello {name}.")
    print(f"You are {age} years old.")
    print(f"Have a good day ahead, {name}.")

greet_name("Prince", 20)
# this gives output as
# Hello Prince.
# You are 20 years old.
# Have a good day ahead, Prince.

# positional arguments
#def my_function(a, b, c):
    #do this with a
    #do this with b
    #do this withc
# keyword arguments
#def my_function(a, b, c):
    #do this with a
    #do this with b
    #do this with c
def greet_name(age= 20, name = "Prince" ): # taks two functions 
    print(f"Hello {name}.")
    print(f"You are {age} years old.")
    print(f"Have a good day ahead, {name}.")
greet_name()
# This gives the ooutput
# Hello Prince.
# You are 20 years old.
# Have a good day ahead, Prince.

# default arguments
#def my_function(a, b, c=5):
    #do this with a
    #do this with b
    #do this with c
# variable arguments
    #def my_function(*args):
    #do this with args



