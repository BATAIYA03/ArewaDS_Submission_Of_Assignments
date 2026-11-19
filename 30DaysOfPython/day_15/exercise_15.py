import requests
import re
from collections import Counter

#level 1
#Question 1
romeo_and_juliet = "https://www.gutenberg.org/files/1112/1112.txt"

response = requests.get(romeo_and_juliet)

text = response.text

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

word_count = Counter(words)

most_common_words = word_count.most_common(10)

print(most_common_words)    

#Question 2
import requests
import statistics

cats_api = "https://api.thecatapi.com/v1/breeds"

response = requests.get(cats_api)
cats = response.json()

weights = []

for cat in cats:
    weight = cat["weight"]["metric"]

    if "-" in weight:
        minimum, maximum = weight.split("-")

        average = (float(minimum) + float(maximum)) / 2

        weights.append(average)

print("Minimum:", min(weights))
print("Maximum:", max(weights))
print("Mean:", statistics.mean(weights))
print("Median:", statistics.median(weights))
print("Standard deviation:", statistics.stdev(weights))

#B
import requests
import statistics

cats_api = "https://api.thecatapi.com/v1/breeds"

response = requests.get(cats_api)
cats = response.json()

lifespans = []

for cat in cats:
    lifespan = cat["life_span"]

    if "-" in lifespan:
        minimum, maximum = lifespan.split("-")

        average = (float(minimum) + float(maximum)) / 2

        lifespans.append(average)

print("Minimum:", min(lifespans))
print("Maximum:", max(lifespans))
print("Mean:", statistics.mean(lifespans))
print("Median:", statistics.median(lifespans))
print("Standard deviation:", statistics.stdev(lifespans))

#C
import requests
from collections import Counter

cats_api = "https://api.thecatapi.com/v1/breeds"

response = requests.get(cats_api)
cats = response.json()

countries = []

for cat in cats:
    country = cat.get("origin")

    if country:
        countries.append(country)

country_frequency = Counter(countries)

for country, frequency in country_frequency.items():
    print(country, ":", frequency)

#level 2
#Question 1
import requests

countries_api = "https://restcountries.com/v3.1/all?fields=name,area"

response = requests.get(countries_api)

countries = response.json()

countries.sort(
    key=lambda country: country.get("area", 0),
    reverse=True
)

for country in countries[:10]:
    print(country["name"]["common"], country.get("area"))

#B
import requests
from collections import Counter

countries_api = "https://restcountries.com/v3.1/all?fields=languages"

response = requests.get(countries_api)

countries = response.json()

languages = []

for country in countries:
    country_languages = country.get("languages", {})

    for language in country_languages.values():
        languages.append(language)

language_count = Counter(languages)

print(language_count.most_common(10))

#C
import requests

countries_api = "https://restcountries.com/v3.1/all?fields=languages"

response = requests.get(countries_api)

countries = response.json()

languages = set()

for country in countries:
    country_languages = country.get("languages", {})

    for language in country_languages.values():
        languages.add(language)

print("Total languages:", len(languages))

#level 3
#Question 1
import requests
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url)

print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.get_text())
