# docstrings
# 1. they are document strings
# 2. they are used to document the code
# 4. written between """  """ or ''' '''.
# 5. can be used as multi liner comments
# 6. can be used to document functions, classes, methods, modules , the purpose of the code, parameters, return values etc
# 7. can be accessed by using help() or the __doc__
def square(number):
    """
    Calculates the square of a given number.

    Parameters:
    number (int or float): The number to be squared.

    Returns:
    int or float: The square of the input number.
    """
    return number ** 2

# Accessing the docstring
print(square.__doc__)
help(square)


