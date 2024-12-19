# # debugging the problem
# # problem no 1
# def my_function():
#     for i in range(1,20):
#         if i == 20:
#             print("You got it.")
# my_function()
# # changing the range from range(1,20) to range(1,21) solves the problem
# # solution is :
# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You got it")
# my_function()

# # problem no 2 
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1,6)
# print(dice_imgs[dice_num])
# # for fixing tthe above code change randint(1,6) to randint(0,5) solves the problem
# # solution is :
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# #problem no 3
# year = int(input("Enter your year of birth:\n"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# # problem arises as the user put the input the year 1994
# # to solve this put year>= 1994 or year<= 1994 in the above code to fix the bug
# # solution is :
# year = int(input("Enter your year of birth:\n"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")


# # problem no 4
# age = input("How old are ypu?:\n")
# if age > 18:
#     print("You can drive at age {age}")
# # problem arises as the user put the input the age 18 and doesn't give output age
# # to solve this put age>= 19 in the above code  and add f string to give age outputto fix the bug
# # solution is :
# age = input("How old are you?:\n")
# if age >= "19":
#     print(f"You can drive at age {age}")


# problem no 5
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page:"))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")

print(total_words)
# fix the bug
# instead of two = , make single =
# solution is :
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page:"))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)


# problem 6
def mutate(a_list):
  b_list = [] 
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
# fix the bug
# the bug is that the new_item is not being added to the list b_list
# solution is :
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)
