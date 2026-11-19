import random
import string

#level 1
#Question 1
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ""

    for i in range(6):
        user_id += random.choice(characters)

    return user_id

print(random_user_id())

#Question2
import random
import string

def user_id_gen_by_user():
    number_of_characters = int(input("Enter number of characters: "))
    number_of_ids = int(input("Enter number of IDs: "))

    characters = string.ascii_letters + string.digits

    for i in range(number_of_ids):
        user_id = ""

        for j in range(number_of_characters):
            user_id += random.choice(characters)

        print(user_id)


user_id_gen_by_user()   

#Question 3
import random

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return f"rgb({red},{green},{blue})"


print(rgb_color_gen())

#level 2
#Question 1
import random
import string

def list_of_hexa_colors(number):
    characters = "0123456789abcdef"
    colors = []

    for i in range(number):
        color = "#"

        for j in range(6):
            color += random.choice(characters)

        colors.append(color)

    return colors


print(list_of_hexa_colors(3))

#Question 2
import random

def list_of_rgb_colors(number):
    colors = []

    for i in range(number):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        color = f"rgb({red},{green},{blue})"

        colors.append(color)

    return colors


print(list_of_rgb_colors(3))

#Question 3
import random

def generate_colors(color_type, number):
    colors = []

    if color_type == "hexa":

        characters = "0123456789abcdef"

        for i in range(number):
            color = "#"

            for j in range(6):
                color += random.choice(characters)

            colors.append(color)

    elif color_type == "rgb":

        for i in range(number):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

            color = f"rgb({red},{green},{blue})"

            colors.append(color)

    else:
        return "Invalid color type"

    return colors


print(generate_colors("hexa", 3))
print(generate_colors("hexa", 1))

print(generate_colors("rgb", 3))
print(generate_colors("rgb", 1))

#level 3
#Question 1
import random

def shuffle_list(items):
    random.shuffle(items)
    return items


numbers = [1, 2, 3, 4, 5, 6]

print(shuffle_list(numbers))

#Question 2
import random

def seven_random_numbers():
    numbers = random.sample(range(10), 7)
    return numbers


print(seven_random_numbers())