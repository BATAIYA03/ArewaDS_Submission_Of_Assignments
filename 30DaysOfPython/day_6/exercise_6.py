#Question 1
dog = {}
dog['Name'] = 'buddy'
dog["color"] = "brown"
dog["breed"] = "Bull Dog"
dog["legs"] = "perfect"
dog["age"] = 10
print(dog)

#Question 2
student = {}
student["First_Name"] = "Muhammad"
student["last_Name"] = "Bataiya"
student["Gender"] = "Male"
student["Age"] = 23
student["Marital Status"] = "Single"
student["Skills"] = ["Python", "JavaScrypt", "HTML"]
student["Country"] = "Nigeria"
student["City"] = "Kano"
student["Address"] = "Hotoro Ramin Kwalabe, Kano"
print(student)

print(len(student))

skills_values = student["Skills"]
print(skills_values)

print(type(skills_values))

student["Skills"].append("CSS")
student["Skills"].append("C")
student["Skills"].append("C++")
print(student)

print(student.keys())
print(student.values())

print(student.items())


del student["Marital Status"]
print(student)

del dog