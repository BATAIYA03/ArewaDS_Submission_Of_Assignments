#level 1
#Question 1
for number in range(11):
    print(number)
#using while loop
number = 0

while number <= 10:
    print(number)
    number += 1

#Question 2
for number in range(10, -1, -1):
    print(number)
#using while loop
number = 10

while number >= 0:
    print(number)
    number -= 1

#Question 3
for number in range(1, 8):
    print("#" * number)

#Question 4
for row in range(8):
    for column in range(8):
        print("#", end=" ")
    print()

#Question 5
for number in range(11):
    print(number, "x", number, "=", number * number)

#Question 6
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)

#Question 7
for number in range(101):
    if number % 2 == 0:
        print(number)

#Question 8
for number in range(101):
    if number % 2 != 0:
        print(number)

#level 2
#Question 1
total = 0

for number in range(101):
    total += number

print("The sum of all numbers is", total)

#Question 2
sum_even = 0
sum_odd = 0

for number in range(101):
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

print("The sum of all evens is", sum_even)
print("The sum of all odds is", sum_odd)

#level 3
#Question 1
countries = ["Finland", "Sweden", "Denmark", "Norway", "Iceland"]
for country in countries:
    if "land" in country:
        print(country)

#Question 2
fruits = ['banana', 'orange', 'mango', 'lemon']

reversed_fruits = []

for fruit in fruits:
    reversed_fruits.insert(0, fruit)

print(reversed_fruits)

#Question 3
languages = set()
countries_data = {
    "Finland": {"languages": ["Finnish", "Swedish"]},
    "Sweden": {"languages": ["Swedish"]},
    "Denmark": {"languages": ["Danish"]},
    "Norway": {"languages": ["Norwegian"]},
    "Iceland": {"languages": ["Icelandic"]}
}

for country in countries_data:
    for language in country["languages"]:
        languages.add(language)

print("Total number of languages:", len(languages))

#B
language_count = {}

for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

sorted_languages = sorted(
    language_count.items(),
    key=lambda item: item[1],
    reverse=True
)

for language in sorted_languages[:10]:
    print(language)

#c
sorted_countries = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True
)

for country in sorted_countries[:10]:
    print(country["name"], country["population"])

