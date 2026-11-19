

#level 1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Question 1
""""
1. Explain the difference between map, filter and reduce.
Answer:
- map() changes or transforms every item in a list.
- filter() selects items based on a condition.
- reduce() combines all items to produce one result. """

#Question 2
"""
2. Explain the difference between higher order function, closure and decorator.
Answer:

Higher Order Function: A function that accepts another function as an argument or returns another function.

Closure: A function that remembers variables from its outer function, even after the outer function has finished executing.

Decorator: A function that modifies or extends the behaviour of another function without changing its original code.
"""

#Question 3
def square(number):
    return number ** 2

def is_even(number):
    return number % 2 == 0

def add_numbers(x, y):
    return x + y

#Question 4
for country in countries:
    print(country)

#Question 5
for name in names:
    print(name)

#Question 6
for number in numbers:
    print(number)

#level 2
#Question 1
result = map(str.upper, countries)

print(list(result))

#Question 2
result = map(lambda number: number ** 2, numbers)

print(list(result))

#Question 3
result = map(str.upper, names)

print(list(result))

#Question 4
result = filter(lambda country: 'land' not in country, countries)

print(list(result))

#Question 5
result = filter(lambda country: len(country) == 6, countries)

print(list(result))

#Question 6
result = filter(lambda country: len(country) >= 6, countries)

print(list(result))

#Question 7
result = filter(lambda country: country.startswith('E'), countries)

print(list(result))

#Question 8
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(
    lambda x, y: x + y,
    filter(
        lambda number: number % 2 == 0,
        map(lambda number: number ** 2, numbers)
    )
)

print(result)

#question 9
def get_string_lists(items):
    result = filter(lambda item: isinstance(item, str), items)

    return list(result)


mixed_list = [1, 'Python', 2, 'Java', 3, 'Flask']

print(get_string_lists(mixed_list))

#question 10
from functools import reduce

result = reduce(lambda x, y: x + y, numbers)

print(result)

#question 11
from functools import reduce

result = reduce(
    lambda x, y: x + ', ' + y,
    countries
)

print(result + ' are north European countries.')

#question 12
def categorize_countries(countries, pattern):
    result = filter(lambda country: pattern in country, countries)

    return list(result)


print(categorize_countries(countries, 'land'))

#question 13
def count_countries_by_initial(countries):
    result = {}

    for country in countries:
        first_letter = country[0]

        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1

    return result


print(count_countries_by_initial(countries))

#Question 14
def get_first_ten_countries(countries):
    return countries[:10]


print(get_first_ten_countries(countries))

#Question 15
def get_last_ten_countries(countries):
    return countries[-10:]


print(get_last_ten_countries(countries))

#level 3
#  Question 1
sorted_by_name = sorted(
    countries_data.countries_data,
    key=lambda country: country['name']
)

for country in sorted_by_name:
    print(country['name'])

#B
sorted_by_capital = sorted(
    countries_data.countries_data,
    key=lambda country: country['capital']
)

for country in sorted_by_capital:
    print(country['name'], country['capital'])

#C
sorted_by_population = sorted(
    countries_data.countries_data,
    key=lambda country: country['population'],
    reverse=True
)

for country in sorted_by_population:
    print(country['name'], country['population'])

#Question 2
language_count = {}

for country in countries_data.countries_data:
    for language in country['languages']:
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


#