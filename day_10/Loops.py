# Day 10 - 30DaysOfPython Challenge
# Loops

#Exercises: Level 1
#question 1 & 2
for i in range(11):
    print(i)

i = 0
while i < 11:
    print(i)
    i += 1

for i in range(10,-1,-1):
    print(i)

i=0
while i < 11:
    print(10-i)
    i += 1

#question 3 
for i in range(1, 8):
    print(i * '#')

for i in range(1, 8):
    print('#' * i)

#question 4
for i in range(8):          
    for j in range(8):      
        print("#", end=" ")
    print()                 

#question 5
for i in range(11):
    print(i, "x", i, "=", i*i)

#question 6
list1=["Python", "Numpy","Pandas","Django", "Flask"]
for item in list1:
    print(item)
    
#question 7 & 8
for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(101):
    if i % 2 != 0:
        print(i)

#Exercises: Level 2
#question 1
total_sum=0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers from 0 to 100 is {total_sum}")

#question 2
total_sum_even=0
total_sum_odd=0
for i  in range(101):
    if i % 2 == 0:
      total_sum_even += i
    if i % 2 != 0:
        total_sum_odd += i
print(f"The sum of all evens is {total_sum_even}. And the sum of all odds is {total_sum_odd}.")

#question 3