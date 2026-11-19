#Question 1
age = int(input("Enter Your Age: "))
if age >= 18:
    print("You're old enough to drive")
else:
    print("Sorry, WAit until you reach 18 years of age")


#Questin 2
my_age = 25

your_age = int(input("Enter your age: "))

if your_age > my_age:
    difference = your_age - my_age

    if difference == 1:
        print("You are 1 year older than me")
    else:
        print(f"You are {difference} years older than me")

elif my_age > your_age:
    difference = my_age - your_age

    if difference == 1:
        print("I am 1 year older than you")
    else:
        print(f"I am {difference} years older than you")
else:
    print("We are the same age!")

#Question 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")

elif a < b:
    print(f"{a} is smaller than {b}")

else:
    print(f"{a} is equal to {b}")


#level 2
#Question 1
score = int(input("Enter your score: "))

if score >= 80:
    print("Grade A")

elif score >= 70:
    print("Grade B")

elif score >= 60 :
    print("Grade C")

elif score >= 50:
    print("Grade D")

elif score >= 0:
    print("Grade F")
else:
    print("Invalid score")

#Question 2
month = input("Enter a month: ")

if month == "September" or month == "October" or month == "November":
    print("The season is Autumn")

elif month == "December" or month == "January" or month == "February":
    print("The season is Winter")

elif month == "March" or month == "April" or month == "May":
    print("The season is Spring")

elif month == "June" or month == "July" or month == "August":
    print("The season is Summer")

else:
    print("Invalid month")

#Question 3
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list")

else:
    fruits.append(fruit)
    print("Fruit added successfully")

print(fruits)

#level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


# 1. Check if the person dictionary has a skills key.
# If yes, print the middle skill.

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])


# 2. Check if the person has Python skill.

if 'skills' in person:
    print("Has Python:", 'Python' in person['skills'])

# 3. Check if backend user, frontend user, or fullstack developer.
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print("He is a front end developer")

elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print("He is a backend developer")

elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print("He is a fullstack developer")

else:
    print("Unknown title")

# 4. If the person is married and if he lives in Finland, print the information in the following format:
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}.")