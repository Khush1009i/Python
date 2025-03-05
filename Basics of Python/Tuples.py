# Tuples in Python: 
# A built-in data type that lets us create 
# immutable sequence of values

# Tuple Methodes
# |----------------|---------------------------------|
# |tup.index( el ) |returns index of first occurance |
# |tup.count(el)   |counts total occurances          |
# |----------------|---------------------------------|

tup1 = (2,3,5,1)
print(type(tup1))
print(tup1)
tip2 = ()

print(type(tip2))
print(tup1[1 : 3])




tup = (1, 2, 4, 6, 8,)
print(tup.index(2))
print(tup.count(2))

# Q10. WAP to ask user to enter names of their 3 fav movies & store them in a list:---------------------------------#
listOfMovies = []
movie1 =input("Enter 1st fav movie: ")
movie2 =input("Enter 2nd fav movie: ")
movie3 =input("Enter 3rd fav movie: ")
listOfMovies.append(movie1)
listOfMovies.append(movie2)
listOfMovies.append(movie3)

print(listOfMovies)

# Q11. WAP to check if a list contains a palindrome of elements:----------------------------------------------------#

list = [1,4,3,4,1]
list1 = [1,3,5,7,9]

copy_List1 = list1.copy()
copy_List1.reverse()


if(copy_List1 == list1 ):
    print("it's palindrome.")
else:
    print("it's not palindrome. ")

