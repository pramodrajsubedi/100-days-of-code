#data structure is a way of organizing and storing the data
#data types are the types of data that can be stored in a data structure
#data types in python are
#1. Integers
#2. Floats
#3. Strings
#4. Boolean
#5. List
#6. Tuple
#7. Dictionary
#8. Set
#9. Complex Numbers
#10. Bytes
#11. NoneType


#lists are always in the form []

name_of_fruits = ["Apple", "Banana", "Mango","Apricot"] # an example of list
#1st item in the list is accesed by variable[0], second by variable[1], and so on
#last item can be accessed by either using names_of_fruits[3] or names_of_fruits[-1].
# to change the any element of the above list
name_of_fruits[1] = "Papaya"
print(name_of_fruits) # prints the updated list
# to add any elment in the list use append function
name_of_fruits.append("Grapes")
print(name_of_fruits) # prints the updated list
# to remove any element from the list use remove function
name_of_fruits.remove("Banana")
print(name_of_fruits) # prints the updated list
# to get the length of the list use len() function
print(len(name_of_fruits)) # prints the length of the list
# to get the index of any element in the list use index() function
print(name_of_fruits.index("Mango")) # prints the index of the element "Mango
# to check if any element is present in the list use in keyword
print("Apple" in name_of_fruits) # prints True if the element is present in the
# list otherwise it prints False
# to sort the list use sort() function
name_of_fruits.sort()
print(name_of_fruits) # prints the sorted list
# to reverse the list use reverse() function
name_of_fruits.reverse
print(name_of_fruits) # prints the reversed list
# to copy the list use copy() function
name_of_fruits_copy = name_of_fruits.copy()
print(name_of_fruits_copy) # prints the copied list


vegetables = ["Pumpkin", "carrot", "spinach", "Mushroom"]
fru_veg= [name_of_fruits,vegetables]
print(fru_veg) # prints the list of lists


