#Day 6 -30DaysOfPython 
#Tuples

#Exercises: Level 1

#Question 1 to 5
tpl = ()

Brothers = ('DevG', 'Hari', 'Adithya')
Sisters = ('Ashly', 'Anu')
siblings = Brothers + Sisters
print(f'Your siblings are: {len(siblings)}')

parents = ('Girish', 'Beena')
family_members = siblings + parents
print(f'Your family members are: {(family_members)}')

#Exercises: Level 2

#Question 1 to 7
*siblings, father, mother = family_members
parents = (father, mother)
print(f'siblings: {siblings}')
print(f'parents: {parents}')

fruit = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'egg')
food_stuff_tp = fruit + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

if len(food_stuff_tp) %2 == 0:
    print(f'Even ,{food_stuff_tp[len(food_stuff_tp) // 2 - 1]} and {food_stuff_tp[len(food_stuff_tp) // 2]} are the middle items')
else:
    print(f'Odd, {food_stuff_tp[len(food_stuff_tp) // 2]} is the middle item')

first_3 = food_stuff_lt[:3]
last_3 = food_stuff_lt[-3:]
print(f'First three items: {first_3}'
      f'\nLast three items: {last_3}')

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f'Estonia in nordic countries: {"Estonia" in nordic_countries}')
print(f'Iceland in nordic countries: {"Iceland" in nordic_countries}')