# List comprehension = A concise way to create lists in python.print
#  compact & eaasier to read than traditional for loop.
# [expression for item in iterable if condition] 



# double = []
# for x in range(1, 10):
#     double.append(x * 2)


# print(double)


doubles = [ x * 2 for x in range(1,11) ]
triples = [ x * 3 for x in range(1,11) ]
square =  [  z * z for z in range(1,10)]
# print(square)



# fruits =[ fruit.upper() for fruit in [ 'apple', 'banana', 'cherry',  'mango']]
# print(fruits)


numbers = [-1, 2, -4, 7, 0,-8, 9, 10, -11, 12]

positive_nums = [num for num in numbers if num >= 0 ]
negative_nums = [num for num in numbers if num < 0  ]
even_nums     = [num for num in numbers if num%2 ==0]
odd_nums      = [num for num in numbers if num%2 ==1]

# print(f"Positive list : {positive_nums}")
# print(f"Negative list : {negative_nums}")
# print(f"Even list     : {even_nums}")
# print(f"Odd  list     : {odd_nums}")


grades =[85, 42, 79, 90, 56, 61, 32]

passing_grades = [grade for grade in grades if grade >= 56]

print(passing_grades)