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

#question 2
my_age = 21
your_age = int(input("Enter your age: "))
age_diff = your_age - my_age
if your_age > my_age:
    print(f"You are {age_diff} years older than me.")
elif your_age < my_age:
    print(f"I am {abs(age_diff)} years older than you.")
else:
    print("We are the same age.")

#question 3
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

#Exercises: Level 2
#question 1
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#question 2
month = input("Enter the month: ")
if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
else:
    print("The season is Summer.")

#question 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("That fruit is already in the list.")
else:
    fruits.append(fruit)
    print("Fruit added to the list.")
    print(f"Updated fruit list: {fruits}")

#Exercises: Level 3
#question 1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print(f"middle skill: {person['skills'][len(person['skills']) // 2]}")

if 'skills' in person :
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

skills = set(person.get("skills", []))
print(skills)
if skills == {"JavaScript", "React"}:
    print("Frontend developer")
elif skills == {"Node", "Python", "MongoDB"}:
    print("Backend developer")
elif {"React", "Node", "MongoDB"}.issubset(skills):
    print("Fullstack developer")
else:
    print("Unknown title")

if person.get("is_marred") and person.get("country") == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
