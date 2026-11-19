#level 1
#Question 1
def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(5, 10))

#Question 2
def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area

print(area_of_circle(7))

#Question 3
def add_all_nums(*args):
    total = 0

    for num in args:
        if not isinstance(num, (int, float)):
            return "All arguments must be numbers"

        total += num

    return total

print(add_all_nums(2, 3, 4, 5))
print(add_all_nums(2, 3, "Hello"))

#Question 4
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(30))

#Question 5
def check_season(month):
    if month in ["September", "October", "November"]:
        return "Autumn"

    elif month in ["December", "January", "February"]:
        return "Winter"

    elif month in ["March", "April", "May"]:
        return "Spring"

    elif month in ["June", "July", "August"]:
        return "Summer"

    else:
        return "Invalid month"

print(check_season("January"))
print(check_season("July"))

#Question 6
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope is undefined"

    slope = (y2 - y1) / (x2 - x1)
    return slope

print(calculate_slope(2, 3, 4, 7))

#Question 7
import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2

    elif discriminant == 0:
        x = -b / (2*a)
        return x

    else:
        return "No real solutions"

print(solve_quadratic_eqn(1, -5, 6))

#Question 8
def print_list(items):
    for item in items:
        print(item)

print_list(["Python", "Java", "C++", "JavaScript"])

#Question 9
def reverse_list(items):
    reversed_items = []

    for item in items:
        reversed_items.insert(0, item)

    return reversed_items

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

#Question 10
def capitalize_list_items(items):
    capitalized = []

    for item in items:
        capitalized.append(item.capitalize())

    return capitalized

print(capitalize_list_items(["python", "java", "flask"]))

#Question 11
def add_item(items, item):
    items.append(item)
    return items

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']

print(add_item(food_staff, 'Meat'))

#Question 12
def remove_item(items, item):
    if item in items:
        items.remove(item)

    return items

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']

print(remove_item(food_staff, 'Mango'))

#Question 13
def sum_of_numbers(n):
    total = 0

    for number in range(n + 1):
        total += number

    return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Question 14
def sum_of_odds(n):
    total = 0

    for number in range(n + 1):
        if number % 2 != 0:
            total += number

    return total

print(sum_of_odds(10))

#Question 15
def sum_of_even(n):
    total = 0

    for number in range(n + 1):
        if number % 2 == 0:
            total += number

    return total

print(sum_of_even(10))

#level 2
#Question 1
def evens_and_odds(n):
    evens = 0
    odds = 0

    for number in range(n + 1):
        if number % 2 == 0:
            evens += 1
        else:
            odds += 1

    print("The number of odds are", odds)
    print("The number of evens are", evens)

evens_and_odds(100)

#Question 2
def factorial(n):
    result = 1

    for number in range(1, n + 1):
        result *= number

    return result

print(factorial(5))

#Question 3
def is_empty(value):
    return len(value) == 0

print(is_empty([]))
print(is_empty("Python"))

#Question 4
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle = length // 2

    if length % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]


def calculate_mode(numbers):
    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    highest = max(frequency.values())

    modes = []

    for number in frequency:
        if frequency[number] == highest:
            modes.append(number)

    return modes


def calculate_range(numbers):
    return max(numbers) - min(numbers)


def calculate_variance(numbers):
    mean = calculate_mean(numbers)

    total = 0

    for number in numbers:
        total += (number - mean) ** 2

    return total / len(numbers)


def calculate_std(numbers):
    return calculate_variance(numbers) ** 0.5


numbers = [1, 2, 3, 4, 5, 5, 6]

print("Mean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Standard deviation:", calculate_std(numbers))

#level 3
#Question 1
def is_prime(n):
    if n <= 1:
        return False

    for number in range(2, n):
        if n % number == 0:
            return False

    return True

print(is_prime(7))
print(is_prime(10))

#Question 2
def all_unique(items):
    for item in items:
        if items.count(item) > 1:
            return False

    return True

print(all_unique([1, 2, 3, 4]))
print(all_unique([1, 2, 2, 3]))

#Question 3
def same_data_type(items):
    if len(items) == 0:
        return True

    first_type = type(items[0])

    for item in items:
        if type(item) != first_type:
            return False

    return True

print(same_data_type([1, 2, 3, 4]))
print(same_data_type([1, "Python", 3]))

#Question 4
def is_valid_variable(variable):
    return variable.isidentifier() and not variable in [
        "False", "None", "True", "and", "as", "assert",
        "async", "await", "break", "class", "continue",
        "def", "del", "elif", "else", "except", "finally",
        "for", "from", "global", "if", "import", "in",
        "is", "lambda", "nonlocal", "not", "or", "pass",
        "raise", "return", "try", "while", "with", "yield"
    ]

print(is_valid_variable("first_name"))
print(is_valid_variable("2name"))
print(is_valid_variable("first-name"))

#Question 5A
def most_spoken_languages(countries_data, number):
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

    return sorted_languages[:number]

#B
def most_populated_countries(countries_data, number):
    sorted_countries = sorted(
        countries_data,
        key=lambda country: country["population"],
        reverse=True
    )

    result = []

    for country in sorted_countries[:number]:
        result.append({
            "country": country["name"],
            "population": country["population"]
        })

    return result

#part2 list comprehension
#Question 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
result = [number for number in numbers if number <= 0]

print(result)

#Question 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
result = [
    number
    for outer_list in list_of_lists
    for inner_list in outer_list
    for number in inner_list
]

print(result)

#Question 3
result = [
    (number, 1, number**1, number**2, number**3, number**4, number**5)
    for number in range(11)
]

print(result)

#Question 4
countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

result = [
    [country.upper(), country[:3].upper(), city.upper()]
    for inner_list in countries
    for country, city in inner_list
]

print(result)

#Question 5
result = [
    {"country": country.upper(), "city": city.upper()}
    for inner_list in countries
    for country, city in inner_list
]

print(result)

#Question 6
names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')]
]
result = [
    first_name + " " + last_name
    for inner_list in names
    for first_name, last_name in inner_list
]

print(result)

#Question 7
# Calculate slope
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

print(slope(2, 3, 4, 7))

#To calculate y intercept
# y = mx + c
y_intercept = lambda x, y, m: y - (m * x)

print(y_intercept(2, 7, 3))
