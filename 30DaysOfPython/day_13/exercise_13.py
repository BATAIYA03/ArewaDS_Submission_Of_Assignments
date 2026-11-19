from datetime import datetime, date, time, timedelta

#Question 1
from datetime import datetime

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print("Day:", day)
print("Month:", month)
print("Year:", year)
print("Hour:", hour)
print("Minute:", minute)
print("Timestamp:", timestamp)

#Question 2
from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

print(formatted_date)

#Question3
from datetime import datetime

date_string = "5 December, 2019"

date_object = datetime.strptime(date_string, "%d %B, %Y")

print(date_object)

#Question 4
from datetime import datetime

now = datetime.now()

new_year = datetime(now.year + 1, 1, 1)

time_difference = new_year - now

print("Time left for New Year:", time_difference)

#Question5
from datetime import datetime

start_date = datetime(1970, 1, 1)

now = datetime.now()

time_difference = now - start_date

print("Time difference:", time_difference)

#Question6
"""
Exercise 6: What can you use the datetime module for?
Answer:

The datetime module can be used for:
1. Time series analysis.
2. Recording timestamps of activities in applications.
3. Adding dates to blog posts.
4. Scheduling events and reminders.
5. Calculating the duration between two dates.
6. Managing registration dates and deadlines.
For example, in a Flask application, you can record when a user creates an account.
"""

#part2 file handling
#level 1
#Question 1
def count_lines_words(filename):

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    words = text.split()

    number_of_lines = len(lines)
    number_of_words = len(words)

    print("Number of lines:", number_of_lines)
    print("Number of words:", number_of_words)


count_lines_words("./data/obama_speech.txt")
count_lines_words("./data/michelle_obama_speech.txt")
count_lines_words("./data/donald_speech.txt")
count_lines_words("./data/melina_trump_speech.txt")

#Question 2
import json

def most_spoken_languages(filename, number):

    with open(filename, "r", encoding="utf-8") as file:
        countries = json.load(file)

    language_count = {}

    for country in countries:
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


print(most_spoken_languages("./data/countries_data.json", 10))

print(most_spoken_languages("./data/countries_data.json", 3))

#Question 3
import json

def most_populated_countries(filename, number):

    with open(filename, "r", encoding="utf-8") as file:
        countries = json.load(file)

    sorted_countries = sorted(
        countries,
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


print(most_populated_countries("./data/countries_data.json", 10))

print(most_populated_countries("./data/countries_data.json", 3))

#level 2
#Question 1
import re

with open("./data/email_exchange_big.txt", "r", encoding="utf-8") as file:
    text = file.read()

email_addresses = re.findall(
    r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}',
    text
)

print(email_addresses)

#Question 2
import re
import os

def find_most_common_words(text_or_file, number):

    if os.path.isfile(text_or_file):
        with open(text_or_file, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = text_or_file

    words = re.findall(r"\b\w+\b", text.lower())

    word_count = {}

    for word in words:

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(
        word_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    result = []

    for word, count in sorted_words[:number]:
        result.append((count, word))

    return result


print(find_most_common_words("./data/sample.txt", 10))

#Question 3
def find_most_frequent_words(filename, number):

    return find_most_common_words(filename, number)


print("Obama's speech:")
print(find_most_frequent_words("./data/obama_speech.txt", 10))

print("\nMichelle Obama's speech:")
print(find_most_frequent_words("./data/michelle_obama_speech.txt", 10))

print("\nTrump's speech:")
print(find_most_frequent_words("./data/donald_speech.txt", 10))

print("\nMelina Trump's speech:")
print(find_most_frequent_words("./data/melina_trump_speech.txt", 10))

#Question 4
import re

def clean_text(text):

    text = text.lower()

    text = re.sub(r"[^a-z\s]", "", text)

    return text.split()


def remove_support_words(words, stop_words):

    result = []

    for word in words:
        if word not in stop_words:
            result.append(word)

    return result


def check_text_similarity(text1, text2, stop_words):

    words1 = clean_text(text1)
    words2 = clean_text(text2)

    words1 = remove_support_words(words1, stop_words)
    words2 = remove_support_words(words2, stop_words)

    set1 = set(words1)
    set2 = set(words2)

    common_words = set1.intersection(set2)
    all_words = set1.union(set2)

    if len(all_words) == 0:
        return 0

    similarity = len(common_words) / len(all_words) * 100

    return similarity


with open("./data/stop_words.txt", "r", encoding="utf-8") as file:
    stop_words = file.read().splitlines()

with open("./data/michelle_obama_speech.txt", "r", encoding="utf-8") as file:
    michelle_speech = file.read()

with open("./data/melina_trump_speech.txt", "r", encoding="utf-8") as file:
    melina_speech = file.read()

result = check_text_similarity(
    michelle_speech,
    melina_speech,
    stop_words
)

print("Text similarity:", result, "%")

#Question 5
print(find_most_common_words("./data/romeo_and_juliet.txt", 10))

#question 6
import csv

python_count = 0
javascript_count = 0
java_count = 0

with open("./data/hacker_news.csv", "r", encoding="utf-8") as file:

    csv_reader = csv.reader(file)

    for row in csv_reader:

        line = " ".join(row)

        if "python" in line.lower():
            python_count += 1

        if "javascript" in line.lower():
            javascript_count += 1

        if "java" in line.lower() and "javascript" not in line.lower():
            java_count += 1


print("Python mentions:", python_count)
print("JavaScript mentions:", javascript_count)
print("Java without JavaScript mentions:", java_count)

