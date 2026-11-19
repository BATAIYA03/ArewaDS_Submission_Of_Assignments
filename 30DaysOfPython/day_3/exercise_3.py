import math

#Module 3
#Question 1
my_age = 23
my_height = 6.5
complex_num = 2 - 4j

#Question 2
base = float(input("Enter the base of the Rectangle: "))
height = float(input("Enter the height of the Rectangle: "))
area_triagle = 0.5 * base * height
print("The Area of the triangle is: ", area_triagle)

#Question 3
side_a = float(input("Enter the first side of the triangle: "))
side_b = float(input("Enter the second side of the triangle: "))
side_c = float(input("Enter the third side of the triangle: "))
peri_meter = side_a + side_b + side_c
print("The Perimeter of the tringle is: ", peri_meter)

#Question 4
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rect_area = length * width
print("The area of the rectangle is: ", rect_area)

#Question 5
rect_perimeter = 2 * (length + width)
print("The perimeter of the rectangle is: ", rect_perimeter)

#Question 6
radius = float(input("Enter the radius of your circle: "))
circle_area = 3.142 * radius * radius
print("The area of the circle is: ", circle_area)

#Question 7
circle_circum = 2 * 3.142 * radius
print("The circumference of the circle is: ", circle_circum)

#Question 8
m = 2 
x_intercept = 2 / 2
y_intercept = -2
print("Slope", m)
print("X_intercept:", x_intercept)
print("Y_intercept:", y_intercept)

#Question 9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print("The slope is: ", slope)
eucledian_distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print("The Euclinian distance between them is: ", eucledian_distance) 

#Question 10
print(m == slope)

#Question 11
for x in range(-5, 2):
    y=x**2+6*x+9
    print("When x=",x, "y=",y)

#Question 12
print(len("python"))
print(len("dragon"))
print(len("python") > len("dragon"))

#Question 13
print("on" in "python" and "on" in "dragon")

#Question 14
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

#Question 15
print("on" not in "dragon" and "on" not in "python")

#Question 16
text = "python"
length = len(text)
float_value = float(length)
string_value = str(float_value)
print(length)
print(float_value)
print(string_value)

#Question 17
number = 10
print(number % 2 == 0)

#Question 18
print(7 // 3 == int(2.7))

#Question 19
print(type("10") == type(10))

#Question 20
print(int(float("9.8")) == 10)

#Question 21
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour"))
pay = hours  * rate
print("Your weekly pay earnings is ", pay)

#Question 22
years = int(input("Enter number of years you lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

#Question 23
for i in range(1, 6):
    print(i,1,i, i**2,i**3)

    