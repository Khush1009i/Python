# Set == collection of un-oredered items,& each are immutable, & unique.
# example == tuple, boolean but dictionary & list are not immutable.



# Set Methods:(Sets are mutable, but the elements of sets are immutable)

#|-----------------------|-----------------------------------|
#|set.add(el)            |add an element                     |
#|set.remove(el)         |removes the element an             |
#|set.clear()            |emptites the set                   |
#|set.pop()              |removes a random value             |
#|set.union(set2)        |combine set value & return new     |
#|set.intersection(set2) |combine common values & return new |
#|-----------------------|-----------------------------------|

#-------------------------------------------------------------------------------------------------------------------#


nums = {1,2,2,3,4,"hello","hello", "world","world"}
print(nums)
print(type(nums))
print(len(nums))

# # empty set:
noom = set()
print(type(noom))


info = {1,2,3,4,6,7}

info.add(5) # adds a new element in set 
info.add("Hello") # adds a new element in set 
print(info)

info.remove(3) # remove an element from a set 
print(info)

info.pop() # removes any random value
print(info)
print(info.pop())

info.clear() # delete all elemant of set 
print(info)

collection = {"Khush", "Priyanka", "Jitu", 2, 3, 4}

print("Union: ",info.union(collection))
print("Intersection : ",info.intersection(collection))

# Q17. Fig out a way to store 9 & 9.0 as seprate values in set.

# one method:
values = { 9, "9.0"}
print(values)

# 2nd method:
value = {"float":9.0, "int":9 }
print(type(value), value)
