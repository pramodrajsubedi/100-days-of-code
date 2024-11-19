# if condition:
#   do this
# else:
#   do this

print("Welcome to the rollercoaster.")
height = int(input("What is your height in cm?: \n"))
bill = 0
if height >= 120:
    age = int(input("Enter your age: \n"))
    if age >= 12:
        bill = 5
        print("The price of tickets for children is $5.")
    elif age <= 18:
        bill = 7
        print("The price of tickets for youth is $7.")
    else :
        bill = 12
        print("The price of tickets for adults is $12.")
    
    for_photo = input("Do you want a photo taken? Y or N:\n")
    if for_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}. Enjoy your ride.")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster.")


# comparision operator
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
