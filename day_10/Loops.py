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

#exercises: Level 3
#question 1

import countries 
for country in countries.countries:
    if 'land' in country:
        print(country)

#question 2
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)
print(reversed_fruits)

#question 3
from countries_data import countries_data as c_data

#What are the total number of languages in the data
n_lang = 0
for i in c_data:
    n_lang += len(i["languages"])
print(f"The total number of languages in the data is {n_lang}.")

#Find the ten most spoken languages from the data
language_count = {}
for languages in c_data:
    for lang in languages["languages"]:
        if lang in language_count:
            language_count[lang] += 1
        else:
            language_count[lang] = 1

# Get the ten most spoken languages
most_spoken = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("The ten most spoken languages are:")
for lang, count in most_spoken:
    print(f"{lang}: {count}")

#Find the 10 most populated countries in the world
populated_countries = sorted(c_data, key=lambda x: x["population"], reverse=True)[:10]
print("The 10 most populated countries are:")
for country in populated_countries:
    print(f"{country['name']}: {country['population']}")