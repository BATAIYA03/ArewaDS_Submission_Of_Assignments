import re

text = "I love Python. Python is interesting."

result = re.findall("Python", text)

print(result)

#level 1
#Question 1
import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph)

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

print(sorted_words)

#Question 2
import re

text = "The positions are -12, -4, -3, -1, 0, 4 and 8."

points = re.findall(r'-?\d+', text)

numbers = [int(point) for point in points]

distance = max(numbers) - min(numbers)

print("Points:", points)
print("Distance:", distance)

#level 2
#Question 1
def is_valid_variable(name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

    return bool(re.match(pattern, name))


print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

#level 3
#Question 1
import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)

    cleaned = re.sub(r'\s+', ' ', cleaned)

    return cleaned


def most_frequent_words(text):
    words = re.findall(r'\b\w+\b', text)

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

    return sorted_words[:3]


cleaned_text = clean_text(sentence)

print(cleaned_text)

print(most_frequent_words(cleaned_text))

