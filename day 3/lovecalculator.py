print("Welcome to the love calculator!")
name_1 = input("Enter the first name : \n")
name_2 = input("Enter the second name : \n")
combined_name = name_1 + name_2
lower_names = combined_name.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit  = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e
score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, Oh ma god turu lob")
elif (score >= 40) or (score <= 50):
    print(f"Your score is {score}, You are alright together")
else:
    print(f"Your score is {score}, Find another match")

