# List Method:
#|--------------------------|----------------------------|
#|list.append()             |add one element at the end  |
#|list.sort()               |sorts in ascending order    |
#|list.sort(reverse = True) |sorts in descending order   |
#|list.reverse()            |reverses list               |
#|list.insert(idx, el)      |insert element at index     |
#|list.remove(1)            |removes 1st ocrnce of elmnt |
#|list.pop(idx)             |removes element at idx      |
#|--------------------------|----------------------------|



list1 = [1,3,5,6,2,0,7,9,8]
list2 = ["b", "a","f","d"]

list2.append("c")
list2.append("e")
list2.sort(reverse= True)
list2.reverse()
list1.reverse()
list1.insert(1,5)
list1.pop(2)
list1.remove(2)

print(list1)
print(list2)