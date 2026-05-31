#day 4
#q1 to q22
q1=['thirty','days','of','python']
result=' '.join(q1)
print(result)

q2=['coding','for','all']
result_2=' '.join(q2)
print(result_2)

variable="coding for all"
print(variable)
length=len(variable)
print(length)
print(variable.upper())
print(variable.lower())
print(variable.capitalize())
print(variable.title())
print(variable.swapcase())
print(variable.find('coding'))
print(variable.index('coding'))
print(variable.replace('coding',  'python'))
print(variable.split(' '))
q14=("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
print(q14.split(', '))
first_char = variable[0]
print("Character at index 0:", first_char)
print("last index: ",variable.rindex('l'))
tenth_char = variable[10]
print("Character at index 10: ", tenth_char)
abbreviation_1='PFE'
abbreviation_2='CFA'
print(variable.index('c'))
print(variable.index('f'))
print(variable.rindex('l'))

#q23 to #q30
q_23='You cannot end a sentence with because because because is a conjunction'
print(q_23.index('because'))
print(q_23.rindex('because'))
print(q_23.replace('because because because', ''))
print(variable.startswith('coding'))
print(variable.endswith('coding'))
q_30='   Coding For All      '
print(q_30.strip())

#q31 to
q_31_a,q_31_b="30DaysOfPython","thirty_days_of_python"
print(q_31_a.isidentifier())
print(q_31_b.isidentifier())

list_32= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result_32='# '.join(list_32)
print(result_32)

q_33="I am enjoying this challenge.\nI just wonder what is next."
print(q_33)

q_34="Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(q_34)

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius,area))
print("The area of a circle with radius %d is %d meters square."%(radius,area))

x,y=8,6
print("sum = %d + %d = %d "%(x,y,x+y))
print("difference = %d - %d = %d "%(x,y,x-y))
print("product = %d * %d = %d "%(x,y,x*y))
print("division = %d / %d = %d "%(x,y,x/y))
print("remainder = %d %% %d = %d "%(x,y,x%y))
print("fdivision = %d // %d = %d "%(x,y,x//y))
print("power = %d ** %d = %d "%(x,y,x**y))
