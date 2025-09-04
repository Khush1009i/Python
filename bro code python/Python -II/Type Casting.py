# Type casting - the process of converting a var from data type to another.
# str(), int(), float(), bool()


# name = "Khush"
# age = 21
# cgpa = 7.9
# is_student = True

# # "type "gives what type of var is it 
# # print(type(name))

# cgpa = int(cgpa) 
# age = float(age)
# age += 1 
# name = bool(name)
#  print(type(name), name)


# User input method
#  input() - funxn type that prompts userr to enter data as their choice
# input() stores data in the form of string

# name = input("what is your name? ")
# age = int(input("What is your age? "))

# print("Hello ",name)
# print("A very good morning!")
# print(f"You are {age} year old ")


# #Exercise 
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: ")) 

# area = length * width
# print(f"Total area of rectangle is: {area}  cm ") 


# Exercise2 - ashopping cart program
item = (input("Enter item you would like to buy? : "))
price = float(input("Price on box? - "))
quantity = int(input("How many would u like- "))
total = price * quantity

print(f"You have bought{quantity} X {item}/s")
print(f"Your Total - {total}$")