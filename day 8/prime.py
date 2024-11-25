#Prime Number Checker
def is_prme(n):
    is_prme = True
    for i in range(2,n):
        if n % i == 0:
            is_prme = False
    if is_prme:
        print("This is a prime number.")
    else:
        print("This is not a prime number")
number = int(input())
is_prme(n = number)