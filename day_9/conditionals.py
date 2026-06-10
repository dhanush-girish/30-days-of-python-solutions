# Day 9 - 30DaysOfPython Challenge
# Conditionals

#Exercises: Level 1
#question 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")