#Day 5 -30DaysOfPython 
#List

#Exercises: Level 1
#Question 1 to 25

empty_list = []

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
print(len(fruits))
print(f"first item : {fruits[0]}")
print(f"middle item : {fruits[2]}")
print(f"last item : {fruits[-1]}")

mixed_data_types = ['Dhanush', 21, 163, {'married': False}, {'country': 'India', 'city': 'Bangalore'}]

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(f"first company : {it_companies[0]}")
print(f"middle company : {it_companies[len(it_companies)//2]}")
print(f"last company : {it_companies[-1]}")

it_companies[0] = 'Nvidia'
print(it_companies)

it_companies.append('Tesla')
print(it_companies)

it_companies.insert(len(it_companies)//2, 'Meta')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print("#; ".join(it_companies))

print("Microsoft" in it_companies)

print(it_companies.sort())
print(it_companies)

print(it_companies.reverse())
print(it_companies)

print(it_companies[0:3])
print(it_companies[-3:])

print(it_companies[len(it_companies)//2])

it_companies.pop(0)
it_companies.pop(-1)
print(it_companies)

del it_companies

#Question 26 & 27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)

#Exercises: Level 2
#question 1 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[-1]
print(f"Min age : {min_age}")
print(f"Max age : {max_age}")

ages.sort()
if len(ages) % 2 == 0:
   print(f"Median age : {(ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2}")
else:
    print(f"Median age : {ages[len(ages)//2]}")

average_age = sum(ages) / len(ages)
print(f"Average age : {average_age}")

print(f"Range of ages : {max_age - min_age}")

print(abs(min_age - average_age) == abs(max_age - average_age))

# Find the middle country(ies) in the countries list
from countries import countries #countries.py file should be in the same directory as lists.py
print(len(countries))
print(f"middle country : {countries[len(countries)//2]}")

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]

print(f"First half : {first_half}")
print(f"Second half : {second_half}")

print(f"Length of first half : {len(first_half)}")
print(f"Length of second half : {len(second_half)}")

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
China, Russia, USA, *scandic = countries_2
print(f'scandic countries : {scandic}')