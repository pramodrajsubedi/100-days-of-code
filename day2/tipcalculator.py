# to calculate the amount of tip to give

print("Welcome to the tip calculator.")
cost = float(input("Please enter the total cost of your meal: \n$"))
people = int(input("How many people are splitting the bill? \n"))
tip_percent = float(input("What percentage of the bill would you like to give as a tip?\n"))
# to calculate the amount of tip to give
tip = (cost * tip_percent) / 100
# to calculate the amount each person needs to pay
total_bill = cost + tip
# to calculate the amount each person needs to pay
bill_per_person = total_bill / people
print(f"Each person needs to pay: ${bill_per_person:.2f}")