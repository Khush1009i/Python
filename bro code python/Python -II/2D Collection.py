# Collection
# syntax sapces are actully important

fruits  =  ["apple", "orange", "banana", ]
vegies  =  {"celery", "carrots", "potatoes"}
fstfood =  ["pizza", "burger", "cakes"]

groceries = [fruits, vegies, fstfood]

# print(groceries[0][1])

for collection in groceries:
    for food in collection:
     print(food, end=" ")
    print()


