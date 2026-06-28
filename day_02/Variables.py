#Day 2: 30 days of python programming
#Variables, Builtin Functions

#Exercises: Level 1
#questions 1 to 13  
first_name = "Dhanush"
last_name = "Girish"
full_name = "Dhanush Girish"
country = "India"
city= "Bangalore"
age = 21
year = 2026
is_married = "Unmarried"
is_true = True
is_light_on = False

gender, year_of_birth = "Male", 2005

#Exercises: Level 2
#Question 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(gender))
print(type(year_of_birth))

#Question 2 & 3
print(len(first_name))
print("comparing lengths:", len(first_name)>len(last_name))

#Question 4 to 11
num_one,num_two = 5, 4

total=num_one+num_two
print("total = ",total)

diff = num_one-num_two
print("difference = ",diff)

product = num_one*num_two
print("product = ",product)

division = num_one/num_two
print("divison = ",division)

remainder = num_one % num_two
print("remainder =", remainder)

exp = num_one**num_two
print("exponent = ",exp)

floor_division = num_one//num_two
print("floor division = ",floor_division)

#Question 12
radius = int(input("Insert radius of the circle : "))
area_of_circle = 3.14 * radius**2
circum_of_circle = 2 * 3.14 * radius
print("Area of circle = ",area_of_circle)
print("Circumference of circle = ",circum_of_circle)

#Question 13
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

#Question 14    
help('keywords')

