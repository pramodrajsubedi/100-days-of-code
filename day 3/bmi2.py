height = float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kgs: \n"))

bmi = float(weight /height**2)
if bmi <= 18.5:
    print(f"Your bmi is " + {bmi} + (".") + "You are underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Your bmi is " + {bmi} + (".") + "You have a normal weight.")
elif bmi >= 25 and bmi <= 29.9:
    print(f"Your bmi is " + {bmi} + (".") + "You are slightly overweight.")
elif bmi >= 30 and bmi <= 34.9:
    print(f"Your bmi is " + {bmi} + (".") + "You are obese.")
else:
    print(f"Your bmi is " + {bmi} + (".") + "You are clinically obese. Join gym ")



 
    


               