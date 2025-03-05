#String Function:
# |----------------------|-----------------------------------------|
# |Function              |Explanation                              |
# |str.endswith("")      |returns true if string ends with substr  |
# |str.capitalize()      |capitalize 1st character                 |
# |str.replace(old,new)  |replaces all occrance of old with new    |
# |str.find(word)        |returns 1st index of ist occurance       |
# |str.count("")         |counts occcurance of substr in string    |
# |----------------------|-----------------------------------------|

str = "i am a coder."
str = str.capitalize()

print(str.endswith("er"))
print(str.capitalize())
print(str.find("a"))
print(str.count("a"))
print(str.replace("o","a"))