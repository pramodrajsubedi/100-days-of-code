#TO CALCULATE THE AVERAGE HEIGHT USING FOR LOOP

students_height = input().split()
# used to collect multiple inputs in a single line, which are separated by spaces.
# input() will capture this(input by user) as a single string.
# split() will break this string into a list of substrings.
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
    total_height = 0
for height in students_height:
    total_height += height
print(f"total_height =  {total_height}")
number_of_students = 0
for student in students_height:
    number_of_students += 1
print(f"number of students  = {number_of_students}")

avg_height = round(total_height/number_of_students)
print(f"average height = {avg_height}")

