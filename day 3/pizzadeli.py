# write a code for pizza delivery

print("Welcome to the Yummy pizza deliveries.\n We deliver pizzas to your doorstep.\n")
bill = 0
size = input("What size of pizza do you want? S, M or L:\n")
pepperoni = input("Do you want pepperoni?: Y or N\n")
extra_cheese= input("Do you need extra cheese?: Y or N\n")
if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"Your total bill is:${bill}")
        else:
         print(f"Your total bill is:${bill}")
    else:
        print(f"Your total bill is:${bill}")
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your total bill is:${bill}")
        else:
           print(f"Your total bill is:${bill}")
    else:
        print(f"Your total bill is:${bill}")
else:
    bill += 25
    if pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your total bill is:${bill}")
        else:
           print(f"Your total bill is:${bill}")
    else:
        print(f"Your total bill is:${bill}")
