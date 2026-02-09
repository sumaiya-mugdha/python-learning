#dictionary
info={
    "name":"mugdha",
    "age":18,
    "balance": 16000.9,
    "marks": 40,
    "subjects":["python","c", "java"], #can access list and tuple
    30: 20
}
print(info)
print(type(info))
print(info["name"])
print(info["marks"])

#nested dictionary
student={
    "name":"mugdha",
    "age":18,
    "marks":{
        "physics":40,
        "chemistry":30,
        "math":50
    },
    "balace":43.67
}
print(student)
print(student["name"])
print(student["marks"])
print(student["marks"]["physics"]) ###for nested dictionary element

#dictionary methods
print(len(student))
print(list(student.keys()))  ###store it like list
print(student.values())
print((student.items()))  ###store it like tuple
pair= (list(student.items()))   ##can store and access like this also
print(pair[0])
student.update({"city":"New York"})
print(student)

print(student.get("make"))   ##works as exception handling. return none not error
print(student.get("name"))


#practice
students = {
    "stu1": {"name": "pinku", "roll": 33, "marks": 95},
    "stu2": {"name": "chilu", "roll": 32, "marks": 91},
    "stu3": {"name": "rinku", "roll": 22, "marks": 76}
}
for student in students.values():
    if student["marks"] > 80:
        print(student["name"])



