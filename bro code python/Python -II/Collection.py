# Collection- a single "variable" used to store multiple values
# List = [] ordered & changable. duplicates OK.
# Set  = {} un-ordered & immutable, but ADD/remove OK. no duplicates.
# Tuple= () ordered & un-chnageable. duplicates OK. Faster




fruits = [ "apple", "banana", "orange", "kiwi" ] 
print(f"{len(fruits)}, {fruits[1]}")
# print(dir(fruits)) - shows the drescription of methods

for fruit in fruits: 
    print(fruit)

print("apple" in fruits) #boolean(gives True or False)
fruits[0] = "pine"
print(fruits[0])