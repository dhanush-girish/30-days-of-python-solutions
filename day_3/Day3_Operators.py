#day 3

#q1 to q3
age=21
height=163.0
complex_number=1+2j

#q4 to q7
b=float(input("enter base = "))
h=float(input("enter height = "))
area=0.5*b*h
print("area of triangle is = ", area)

side_a=int(input("enter side a = "))
side_b=int(input("enter side b = "))
side_c=int(input("enter side c = "))
perimeter=side_a+side_b+side_c
print('perimeter of triangle = ',perimeter)
        
length=int(input("enter length = "))
breadth=int(input("enter breadth = "))
area_of_rectangle=length*breadth
perimeter_of_rectangle= 2*(length+breadth)
print("area of  rectangle = ",area_of_rectangle)
print("perimeter of rectangle = ",perimeter_of_rectangle)

radius=int(input("enter radius = "))
pi=3.14
area_of_circle=pi*radius**2
circumference_of_circle=2*pi*radius
print("area of  circle = ",area_of_circle)
print("circumfernece of circle = ",circumference_of_circle)

#q8 to q10
slope_8= 2
y_intercept= -2
x_intercept= 1
print("--- Question 8 ---")
print("Slope:", slope_8)
print("y-intercept: (0, -2)")
print("x-intercept: (1, 0)")

# --- Question 9 ---
import math
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_9 = (y2-y1)/(x2-x1)
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("\n--- Question 9 ---")
print("Slope:", slope_9)
print("Euclidean Distance:", round(distance, 2))

#q10
print("Are the slopes exactly the same?:", slope_8 == slope_9)

 #q11
a,b,c = 1,6,9
discriminant= (b**2)-4*a*c
x1=(-b + math.sqrt(discriminant))/(2*a)
x2=(-b - math.sqrt(discriminant))/(2*a)
print("the value of 0 when x is : ")
print("x1 =", x1)
print("x2 =", x2)

#q12 to q15
print("Is length of python > dragon?:", len('python') > len('dragon'))
print("Is 'on' in both python and dragon?:", 'on' in 'python' and 'on' in 'dragon')
print("Is jargon in the sentence?:", 'jargon' in 'I hope this course is not full of jargon')
print("Is 'on' missing from both?:", 'on' not in 'python' and 'on' not in 'dragon')

#q16 to 20
py="python"
text_length=len(py)
float_value=float(text_length)
string_value=str(float_value)

num=int(input("enter Number to check : "))
numcheck= num%2==0
print("the number is even : ",numcheck)

fd=7//3
print("floor division answer is : ",fd)
converted=int(2.7)
print("converted 2.7 value = ", converted)
print("comparing if values are same : ",fd==converted)

type("10")==type(10)
print("Is type of '10' equal to type of 10?:", type("10") == type(10))
int(float('9.8'))==10
print("Is int('9.8') equal to 10?:", int(float('9.8')) == 10)

#q21 to 23
hour=int(input("enter Hours : "))
rate=int(input("Enter rate per hour: "))
weekly_earning=hour*rate
print("Your weekly earning is : ",weekly_earning)

years=int(input("Enter number of years you have lived : "))
seconds=years*31536000
print("You have lived for : ",seconds, "seconds")


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

        

