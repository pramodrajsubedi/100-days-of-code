# function with outputs
def my_function():
  result = 3*2
  return result 
# call the function and print the result
print(my_function())  # Output: 6


def format_name(f_name, l_name):
   formated_f_name =f_name.title()
   formated_l_name = l_name.title()
   print(f"{formated_f_name} {formated_l_name}")
format_name("RAmesh", "ShaH")
# this prints out the first letter of every word in capital and rest of the letter in lower case
# Output: Ramesh Shah
# another way
def format_name(f_name, l_name):
   formated_f_name = f_name.title()
   formated_l_name = l_name.title()
   return f"{formated_f_name} {formated_l_name}" # use of the return function
print(format_name("RAMesH", "SHAh"))
# Output: Ramesh Shah

