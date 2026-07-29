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

#question 8 to 15
def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"])) 

def capitalize_list(items):
    for i in items:
        items[items.index(i)] = i.capitalize()
    return items
print(capitalize_list(["hello", "world"]))


def add_item(lst, item):
    lst.append(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
print(add_item(food_stuff, "Meat"))
print(add_item(numbers, 5))

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(food_stuff, "Mango"))
print(remove_item(numbers, 3))

def sum_of_numbers(numbers):
    total = 0
    for num in range(numbers+1):
        total += num
    return total

print(sum_of_numbers(5))  
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))  

def sum_of_odds(number):
    total = 0
    for num in range(number + 1):
        if num % 2 != 0:
            total += num
    return total
print(sum_of_odds(5))

def sum_of_evens(number):
    total = 0
    for num in range(number + 1):
        if num % 2 == 0:
            total += num
    return total
print(sum_of_evens(5))

#Exercises: Level 2

#question 1
def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of evens is {evens} and the number of odds is {odds}"
print(evens_and_odds(100))

#question 2
def factorial(n):
    fac = 1
    for i in range (1, n + 1):
        fac *= i
    return fac
print(factorial(3))

#question 3
def calculate_mean(lst):
    mean = sum(lst) / len(lst) if len(lst) > 0 else 0
    return mean

def calculate_median(lst):
    median = sorted(lst)[len(lst) // 2] if len(lst) > 0 else 0
    return median

def calculate_mode(lst):
    from collections import Counter
    if len(lst) == 0:
        return None
    count = Counter(lst)
    mode_data = count.most_common(1)
    return mode_data[0][0] if mode_data else None

def calculate_range(lst):
    if len(lst) == 0:
        return 0
    return max(lst) - min(lst)

def calculate_variance(lst):
    if len(lst) == 0:
        return 0
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance

def calculate_std_deviation(lst):
    variance = calculate_variance(lst)
    std_deviation = variance ** 0.5
    return std_deviation

print(calculate_mean([1, 2, 3, 4, 5]))
print(calculate_median([1, 2, 3, 4, 5]))
print(calculate_mode([1, 2, 2, 3, 3, 3]))
print(calculate_range([1, 2, 3, 4, 5]))
print(calculate_variance([1, 2, 3, 4, 5]))
print(calculate_std_deviation([1, 2, 3, 4, 5]))