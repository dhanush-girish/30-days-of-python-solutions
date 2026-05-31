#Day 4 -30DaysOfPython 
#Strings

#question 1 to 4
q1=['Thirty','days','of','python']
result=' '.join(q1)
print(result)

q2=['Coding','for','all']
result_2=' '.join(q2)
print(result_2)

company="Coding For All"
print(company)

#question 5 to 22
print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[:6])

print(company.index('Coding'))
print(company.find('Coding'))

print(company.replace('Coding',  'Python'))
print("Python For Everyone".replace("Everyone", "All"))

print(company.split(' '))

q14=("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
print(q14.split(', '))

first_char = company[0]
print("Character at index 0:", first_char)
print("last index: ",company.rindex('l'))
tenth_char = company[10]
print("Character at index 10: ", tenth_char)

phrase_1 = "Python For Everyone"
words_1 = phrase_1.split()
acronym_1 = "".join([word[0] for word in words_1])
print(acronym_1)

phrase_2 = "Coding For All"
words_2 = phrase_2.split()
acronym_2 = "".join([word[0] for word in words_2])
print(acronym_2)

print(company.index('C'))
print(company.index('F'))
print(company.rindex('l'))

#question 23 to 29
q_23='You cannot end a sentence with because because because is a conjunction'
print(q_23.index('because'))
print(q_23.rindex('because'))

sliced_phrase = q_23[31:54]
print(sliced_phrase)

print(company.startswith('Coding'))
print(company.endswith('coding'))

q_30='   Coding For All      '
print(q_30.strip())

#question 31 to 34
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
print("quotient = %d / %d = %.2f" % (x, y, x/y))
print("remainder = %d %% %d = %d "%(x,y,x%y))
print("floor division = %d // %d = %d "%(x,y,x//y))
print("power = %d ** %d = %d "%(x,y,x**y))
