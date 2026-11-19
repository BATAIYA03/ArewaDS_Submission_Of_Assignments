#Module 4
#Question 1
print("Thirty" + " " + "Days" + " " + "Of" + " " "Python")

#Question 2
print("Coding" + " " + "For" + " " + "All")

#Question 3
company = "Coding For All"
print(company)

#Question 4
print(len(company))

#Question 5
print(company.upper())

#Question 6
print(company.lower())

#Question 7
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Question 8
print(company[0:6])

#Question 9
print("Coding" in "Coding for All")

#Question 10
replaced_com = company.replace("Coding", "Python")
print(replaced_com)

#Question 11
text = "Python for Everyone"
print(text.replace("Everyone", "All"))

#Question 12
print(company.split(" "))

#Question 13
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

#Question 14
print(company[0])

#Question 15
print(len(company)- 1)

#Question 16
print(company[10])

#Question 17
text = "Python for Everyone"
acronym = "PFE"
print(acronym)

#Question 18
company = "Coding For All"
acronym = "CFA"
print(acronym)

#Question 19
print(company.index("C"))

#Question 20
print(company.index("F"))

#Question 21
text = "Coding For All People"
print(text.rfind("l"))

#Question 22
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

#Question 22
print(sentence.rindex("because"))

#Question 23
start = sentence.find("because")
end = start + len("because because because")
print(sentence[start:end])

#Question 24
print(sentence.find("because"))

#Question 25
start = sentence.find("because")
end = start + len("because because")
print(sentence[start:end])
 
#Question 26
print(company.startswith("Coding"))

#Question 27
print(company.endswith("coding"))

#Question 28
print(company.strip())

#Question 29
print("30DaysOfCode".isidentifier())
print("thirty_days_of_python".isidentifier())

#Question 30
python_libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("#".join(python_libraries))

#Question 31
print("I am enjoying this challenge\nI just woder what's next")

#Question 32
print("Name\t\tAge\t\tCountry")
print("Asabeneh\t\t250\t\tFinland")

#Question 33
radius = 10
area = 3.142 * radius ** 2
print(f"The area of the circle with radius {radius} is {area}")

#Question 34
a = 8
b = 6
print("{} + {}={}".format(a,b, a+b))
print("{} - {}={}".format(a,b, a-b))
print("{} * {}={}".format(a,b, a*b))
print("{} / {}={:.2f}".format(a,b, a/b))
print("{} % {}={}".format(a,b, a % b))
print("{} // {}={}".format(a,b, a//b))
print("{} ** {}={}".format(a,b, a**b))
