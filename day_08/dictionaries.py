# Day 8 - 30DaysOfPython Challenge
# Dictionaries

#Exercises: Day 8
#question 1 to 11

dog = {}

dog['name'] = 'Pablo'
dog['color'] = 'Black'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print(dog)

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'is_married': False,
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main Street'
}
print(student)

print(len(student))

print(f"Student skills: {student['skills']} and datatype of skills: {type(student.get('skills'))}")

student['skills'].append('React')
student['skills'].append('Node.js')

print(list(student.keys()))
print(list(student.values()))

print(list(student.items()))

student.pop('is_married')
print(student)

del dog