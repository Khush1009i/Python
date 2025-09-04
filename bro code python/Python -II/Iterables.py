# iterable = a obj/collection that can return its element 
#               one at a time, allowing it to be iterated 
#               over in a loop.


numbers = [1,2,3,4,5]
for item in numbers:
    print(item, end=" ")



fruits = {"Apple", "bnanana","coco", "orange"}
for fruit in fruits:
    print(fruit, end=" ")

name = "Khush Soni"
for char in name:
    print(char, end="")


my_dict = {"Khush":1,"Soni":2 }

for key, value in my_dict.items():
    print(f"{key} = {value}")