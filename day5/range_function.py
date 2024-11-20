#USE OF FOR LOOP WITH RANGE FUNCTION
# for number in range(a,b):
#     print(number)


for number in range(1,20):
    print(number)  # prints numbers from 1 to 19


for number in range (1,20,2): #here 2 is a step , prints out the number after two numbers

    print(number)


total = 0
for number in range(1, 101):
    total += number
print(total) # prints the sum of all numbers from 1 to 100


target = int(input())
even_sum = 0
for number in range (2, target+1, 2):
    even_sum += number
print(even_sum) # prints the sum of all even numbers from 2 to the target number
