#Level 1
# Day 2: 30 Days of python programming
import math


first_name = "Muhammad"
last_name = "Abduljalal Bataiya"
full_name = "Muhammad Abduljalal Bataiya"
country = "Nigeria"
city = "Kano"
age = 23
year = 2026
is_married = False
is_true = True
is_light_on = True
name, day, school, hobby, year = "Muhammad", "Tuesday", "ArewaDS Academy", "Writing Codes", 2026

#Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(name))
print(type(day))
print(type(school))
print(type(hobby))

print(len(first_name))

print(len(first_name) == len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
divison = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

#Area of a circle
r = 30
area_of_circle = math.pi * (r ** 2)
print("The area of the circle is: ", area_of_circle)

#Circumference of a circle
circum_of_circle = 2 * math.pi * r
print("The Circumference of the circle is: ", circum_of_circle)

#r as user input
radius = float(input("Enter the radius of the circle"))
a = math.pi * (radius ** 2)
print("The area is: ", a)

first_name = input("Enter your first name")
last_name = input("Enter your last names")
country = input("Enter the country you reside")
age = input("Enter your current age")


