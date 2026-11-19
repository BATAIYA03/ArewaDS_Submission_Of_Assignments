#list level 1
#Question 1
empty_list = []

#Question 2
students = ["MUhammad", "Abubakar", "Khalid", "Sa'idu", "Aliyu"]

#Question 3
print(len(students))

#Question 4
first_item, middle_item, last_item, *rest = students
print(first_item)
print(middle_item)
print(last_item)

#Question 5
mixed_data_types = ["Muhammad", 25, 5.9, "Single", "Kano"]
print(mixed_data_types)  

#Question 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Question 7
print(it_companies)

#Question 8
print(len(it_companies))

#Question 9
print(it_companies[0])  # First company

#Question 10
print(it_companies[len(it_companies) // 2])  # Middle company

#Question 11
print(it_companies[-1])  # Last company

#Question 12
it_companies[0] = "Meta"
print(it_companies)

#  Question 13
it_companies.append("Twitter")
print(it_companies)

#Question 14
it_companies.insert(3, "Tesla")
print(it_companies)

#Question 15
print("Google" in it_companies)

#Question 16
it_companies.sort()
print(it_companies)

#Question 17
it_companies.reverse()
print(it_companies) 

#Question 18
print(it_companies[:3])

#Question 19
print(it_companies[-3:])

#question 20
middle = len(it_companies) // 2

if len(it_companies) % 2 == 0:
    print(it_companies[middle - 1:middle + 1])
else:
    print(it_companies[middle])

#Question 21
it_companies.pop(0)
print(it_companies)

#Question 22
middle = len(it_companies) // 2
it_companies.pop(middle)

print(it_companies)

#Question 23
it_companies.pop()
print(it_companies)

#Question 24
it_companies.clear()
print(it_companies)

#question 25
del it_companies


#sets level 1
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon" }
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["ArewaDS Academy", "Udemy London Bootcamp", "Free Code Camp"])
print(it_companies)

it_companies.remove("IBM")
print(it_companies)

"""While removing an item in a set, if the item is not found;
remove() raises an error while dicard() doesn't raise any error
"""

#level 2
print(A.union(B))

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.update(B))
print(B.update(B))

print(B.symmetric_difference(A))

del A
del B

#level 3
set_age = set(age)
print(len(set_age))
print(len(age)) # The listed age is bigger than the set_age

"""
Strings; is the data type in form of text enclosed by hyphens("" or '')
List; is the representation of datas enclosed in a squared brackect([])
Tuple; is the set of immutable datas enclosed in an brackets()
Set; is the represntation of data in a cali-brackets({})

"""

