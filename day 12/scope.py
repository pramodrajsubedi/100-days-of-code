# scope


enemies = 1 
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope
# it exists within a function.
# it is created when a function is called.
# it is destroyed when a function is finished.
# it is used to store variables that are used within a function.
# it is not accessible outside a function.
# it is used to prevent variables from being accessed or modified outside a function.
# it is used to create a new scope for a function.
# it is used to prevent name clashes between variables in different functions.


#global scope
# it exists outside a function.
# it is created when a program starts.
# it is destroyed when a program ends.
# it is used to store variables that are used outside a function.
# it is accessible inside a function.
# it is used to modify variables that are used outside a function.
# avoid modifying global scope.



#global constants
# they are variables that are used throughout a program.
# they are not modified once they are created.
# they are used to store values that do not change.
# they are used to make a program more readable, maintainable, efficient, scalable, secure.




#namespace
# it is a mapping from names to objects.
# it is used to store variables and functions in a program.
# it is used to prevent name clashes between variables and functions in a program.
# it is used to create a new scope for a function.
# it is used to prevent variables from being accessed or modified outside a function.

