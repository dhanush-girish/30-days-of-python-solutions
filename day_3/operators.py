# Day 3 - 30DaysOfPython Challenge
# Operators

#question 1 to 3
age=int(21)
height=float(173.0)
complex_number=complex(1 + 2j)

#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
b=int(input("Enter base = "))
h=int(input("Enter height = "))
area=0.5*b*h
print("The area of triangle is = ", area)

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle and calculate the perimeter of the triangle (perimeter = a + b + c)
side_a=int(input("Enter side a = "))
side_b=int(input("Enter side b = "))
side_c=int(input("Enter side c = "))
perimeter=side_a+side_b+side_c
print('The perimeter of triangle = ',perimeter)

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))       
length=int(input("Enter length = "))
breadth=int(input("Enter breadth = "))
area_of_rectangle=length*breadth
perimeter_of_rectangle= 2*(length+breadth)
print("Area of  rectangle = ",area_of_rectangle)
print("Perimeter of rectangle = ",perimeter_of_rectangle)

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius=int(input("Enter radius = "))
pi=3.14
area_of_circle=pi*radius**2
circumference_of_circle=2*pi*radius
print("area of  circle = ",area_of_circle)
print("circumfernece of circle = ",circumference_of_circle)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_8= 2
y_intercept= -2
x_intercept= 1
print("Slope:", slope_8)
print("y-intercept: (0, -2)")
print("x-intercept: (1, 0)")

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_9 = (y2-y1)/(x2-x1)
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

print("Slope:", slope_9)
print("Euclidean Distance:",round(distance, 2))

#10. Compare the slopes in tasks 8 and 9.
print("Are the slopes exactly the same?:", slope_8 == slope_9)

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
import math
a,b,c = 1,6,9
discriminant= (b**2)-4*a*c
x1=(-b + math.sqrt(discriminant))/(2*a)
x2=(-b - math.sqrt(discriminant))/(2*a)
print("the value of 0 when x is : ")
print("x1 =", x1)
print("x2 =", x2)

#question 12 to 15
print("Is length of python > dragon?:", len('python') > len('dragon'))
print("Is 'on' in both python and dragon?:", 'on' in 'python' and 'on' in 'dragon')
print("Is jargon in the sentence?:", 'jargon' in 'I hope this course is not full of jargon')
print("Is 'on' missing from both?:", 'on' not in 'python' and 'on' not in 'dragon')

#question 16 to 20
print(str(float(len("python")))) 

num=int(input("enter Number to check : "))
numcheck= num%2==0
print("the number is even : ",numcheck)

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hour=int(input("Enter Hours : "))
rate=int(input("Enter rate per hour: "))
weekly_earning=hour*rate
print("Your weekly earning is : ",weekly_earning)

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years=int(input("Enter number of years you have lived : "))
seconds=years*31536000
print("You have lived for %d seconds" % seconds)


x = 1
print(x, x**0, x**1, x**2, x**3)
x = 2
print(x, x**0, x**1, x**2, x**3)
x = 3
print(x, x**0, x**1, x**2, x**3)
x = 4
print(x, x**0, x**1, x**2, x**3)
x = 5
print(x, x**0, x**1, x**2, x**3)

        

