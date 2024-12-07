# grading Program
student_scores = {
    "Ram":90,
    "Shyam": 25,
    "Hari": 50,
    "Krishna": 75,
    "Rahul": 100,
}
student_grade = {}
for student in student_scores:
    score = student_scores[student]
    if score >= 90:
        student_grade[student]= "Outstanding!"
    elif score >= 80:
        student_grade[student]= "Amazing"
    elif score >= 70:
        student_grade[student]= "acceptabe"
    else:
        student_grade[student]= "Fail"

print(student_grade)


# if i want to know the result of a specified person

name = input("Enter your name: \n")
if name in student_scores:
    print(f"Your grade is {student_grade[name]}")
else:
    print("Sorry, your name is not in the list")

  

        