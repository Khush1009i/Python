# Dictionary in python == dic are used to stroe data values in key:value pairs.
# they are unordered, mutable(un-changeble), & don't allow duplicate keys
# A key can be a string, integer, float value, booleean value, list, tupple.
# dict["name"], dict['cgpa'],dict["marks"]
# dict["key"] = "value"


info = {
    "key" : "value",
    "tag" : "Khush",
    "language" : ["Python","C", "Java", "Javascript"],
    "age" : 35,
    "adult": True,

}
null_dict = {}
print(null_dict)

print(info)
print(type(info))
print(info["tag"])
info["adult"] = False
print(info["adult"])


# Nested Dictionary:
student = {
    "name" : "khush",
    "Semester" :"5th sem",
    "subjects":("phy", "maths", "chem"),
    "subjects_Marks": {
        "phy"   : 33,
        "maths" : 43,
        "chem"  : 50
    }
}

print(student["subjects_Marks"]["phy"])


# Dictionary Methods:
#|----------------------|------------------------------|
#|myDict.keys()         |return all keys               |
#|myDict.values()       |return al values              |
#|myDict.items()        |return all  pairs as tup      |
#|myDict.get("key")     |retuen the key acc to value   |
#|myDict.update(newDict)|insert spec items to the dict |
#|----------------------|------------------------------|

print(student.keys())
print(len(list(student.keys())))
print(len(student))
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("name2"))
print(student["name"]) # if print(student["name2"])#error
print(student.update({"city": "delhi"}))
print(student.get("city"))