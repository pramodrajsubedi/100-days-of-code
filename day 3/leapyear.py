# here we calculate or check whether the given number is leap year or not
year = int(input("Enter the year you want to check : \n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
         print(f"{year} is not a leap year")
    else:
       print(f"{year} is a leap year")
else:
   print(f"{year} is not a leap year")

