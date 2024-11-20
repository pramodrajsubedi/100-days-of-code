# While Loop
# The while loop is used to execute a block of code as long as the condition is true
# Syntax: while condition: code to be executed
# Example:
# while statement_is_true:
#     code_to_be_executed
# it gets executed until the statement is false  


# Examples
#1
n = 1
while n <= 5:
    print("You are greatest of all time")
    n +=1
# this prints out You are greatest of all time
#until n  is less than or equal to 5

#2
# finding fatorial
n = 4
factorial = 1
while n >0:
    factorial *= n
    n -= 1

print("factorial:", factorial)
# user can give their own number with the  code
n = int(input("Enter your desired number:\n"))
factorial = 1
while n > 0:
    factorial *= n  
    n -= 1
print("factorial:", factorial)

    