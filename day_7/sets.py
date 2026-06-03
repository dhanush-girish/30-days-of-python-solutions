# Day 7 - 30DaysOfPython Challenge
# Sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
#question 1 to 5

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Meta', 'Netflix', 'Tesla'])
print(it_companies)

it_companies.pop()
print(it_companies)

"""
.remove(): If the item isn't there, it crashes your program with a KeyError.
.discard(): If the item isn't there, it completely ignores the command and moves on quietly without causing an error.
"""

#Exercises: Level 2
#question 1 to 7

c= A.union(B)
print(c)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A,B,it_companies

#Exercises: Level 3
#question 1 to 3

age_set = set(age)
print(f'comparing the length of age list and age set: {len(age)} > {len(age_set)}')

'''
String: An ordered, immutable collection of characters wrapped in quotes used exclusively for text data.

List: An ordered, mutable (changeable) collection of items wrapped in square brackets [] that allows duplicate values.

Tuple: An ordered, completely immutable (locked) collection of items wrapped in parentheses () that allows duplicate values.

Set: An unordered, mutable collection of items wrapped in curly braces {} that explicitly bans duplicate values and has no index positions.
'''
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_set = set(sentence.split())
print(f'Number of unique words in the sentence: {len(sentence_set)}')
