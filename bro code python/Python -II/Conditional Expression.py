# Conditional Expression a shortcut for if-else statements.
# similar to terniary opertaors...!
# print or assign one of two valuess based on a condition.
# X if condition else Y


num = 5


print( "Positive" if num >=0 else "Negative" )
result = "Even" if num%2 ==0 else "Odd"
print(result)

a=6
b=7
max_num = a if a>b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

age = 25
status ="Adult" if age >=18 else "Child"
print(status)

temp =30
weather = "Hot" if temp >20 else "Cold"
print(weather)

user_role = "Admin"
access_level = "Full access" if user_role =="Admin" else "Limited access"
print(user_role)