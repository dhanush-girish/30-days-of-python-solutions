# Day 11 - 30DaysOfPython Challenge
# Functions

#Exercises: Level 1

#question 1 to 7
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print("The sum is:", add_two_numbers(3, 5)) 

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area
radius = float(input("Enter the radius of the circle: "))
print("The area of the circle is:", area_of_circle(radius))

def add_all_nums(*args):
    for num in args:
        if type(num) != int and type(num) != float:
            return f"Error: {num} is not a number, {num} is of type {type(num)}"
    return sum(args)

print(add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(1, 2, "apple", 4))

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
print(f"The temperature in Fahrenheit is: {convert_celsius_to_fahrenheit(celsius)}")

def check_season(month):
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    elif month in ["September", "October", "November"]:
        return "Autumn"
    else:
        return "Invalid month"

month = input("Enter a month: ").capitalize()
print(f"The season for {month} is: {check_season(month)}")

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    slope = (y2 - y1) / (x2 - x1)
    return slope

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return f"Two real roots: {root1} and {root2}"

#question 8
def print_list(lst):
    for item in lst:
        print(item)
