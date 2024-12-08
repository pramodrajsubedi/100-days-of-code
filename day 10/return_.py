# mmultiple return keyword
def multiply(a, b):
    return a * b
print(multiply(3,4))

#use of multiple return
def multiply(a, b):
    return a * b, a + b, a / b
print(multiply(3,4))  # Output: (12, 7, 0)

# another example for previous code
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide necessary info."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(format_name(input("What is your name?\n"),
                   input("What is your last name?\n")))
