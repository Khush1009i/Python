# write a basic program to demonstrate data type in python



age = 12
salary = 120000.123
old = False 
name = "Khush Soni "

# print(f"datat type of name  {type(name)}")
# print(f"datat type of age   {type(age)}")
# print(f"datat type of old  {type(old)}")
# print(f"datat type of salary  {type(salary)}")



# write a program compute distance between two points by taking input from user :

# distance btw two points:( ((x1 - x2)**2) + ((y2 - y1)**2))**0.5

# print("Enter the following details: ")
# x1 = int(input("Enter the 'x1' point: "))
# y1 = int(input("Enter the 'y1' point: "))

# x2 = int(input("Enter the 'x2' point: "))
# y2 = int(input("Enter the 'y2' point: "))

# X = x2 - x1
# Y = y2 - y1

# distance = (  (X**2) + (Y**2) )**0.5
# print(f"points were: {x1,y1} & {x2,y2}")
# print(f"distance between these two points: {distance}")


## write a program that takes 2 num as command line arguments & its sum 

# num1 = int(input("Enter the point X: "))
# num2 = int(input("Enter the point Y: "))

# sum = num1 + num2

# print(f"You numbers were: 'X'= {num1}, 'Y'= {num2} ")
# print(f"Total sum of numbers: {sum}")



## Write a program for checking wether the given num is an even or not ?


# number = int(input("Enter the number: "))
# if number % 2 == 0:
#     print(f" Number {number} is an Even number" )
# else:
#     print(f" Number {number} is an odd number" )


# WAP using a loop that prints out the decimal equi of 1/2, 1/3, 1/4...1/10.

# for i in range(1, 11 ): 
#     decimal_value = 1 / i
#     print(f" 1/{i} = {decimal_value: .2f}")



# WAP to demonstrate list & tuple in python.

# name = ["Khush","Adam", "Johnny", "Dean"]
# last_name = {"Soni", "Sandler", "Walker","Martine"}
# short_name = ("KS", "AS","JW", "DM")

# print(type(name))
# print(type(last_name))
# print(type(short_name))

# WAP using loop that loops over a sequence
# name = ["Khush","Adam", "Johnny", "Dean"]
# for names in name:
#     print(names)


# WAP using while loop that ask user for a number, & prints countdown from teh number to zero
# number = int(input("Enter the starting countdown number: "))

# while number >= 0:
#     print(number)
#     number -= 1


# WAP that find sum of all prime below 2 million 

# def is_prime(n):
#     if n < 2 or (n > 2 and n % 2 == 0): return False
#     return all(n % i for i in range(3, int(n**0.5) + 1, 2))

# def sum_of_primes(limit):
#     return sum(n for n in range(2, limit) if is_prime(n))

# print(sum_of_primes(2_000_000))


# by considering the terms in Fibonacci seq whose value don't exceed 4mill .WAP to find that number to zero
# def sum_fibonacci(limit):
#     a, b, total = 0, 1, 0
#     while b < limit:
#         total += b
#         a, b = b, a + b
#     return total

# print(sum_fibonacci(4_000_000))


# wap  to count number of charcters in string and store them in a dictionary data structure

# string = input("Enter any name/ character: ")
# character = {}
# for char in string:
#     character[char] = character.get(char,0) + 1
# print(character)


# string = input("Enter a string: ")
# char_count = {}

# for char in string:
#     char_count[char] = char_count.get(char, 0) + 1

# print(char_count)

# wap to use split & join methods in string & store 
# & trace a birthday of a person with dicitionary data structure

# Creating a dictionary to store names & birthdays
# Dictionary to store birthdays
# birthdays = {}

# # Taking multiple inputs separately
# n = int(input("How many birthdays do you want to enter? "))

# for _ in range(n):
#     name = input("Enter name: ").strip()
#     dob = input("Enter birthday (DD/MM/YYYY): ").strip()
    
#     if name and dob:  # Ensuring inputs are not empty
#         birthdays[name] = dob
#     else:
#         print("Invalid input! Both Name and Birthday are required.")

# # Searching for a birthday
# search_name = input("\nEnter a name to find the birthday: ").strip()
# print(f"{search_name}'s Birthday: {birthdays.get(search_name, 'Not found!')}")

# # Display all stored birthdays
# print("\nAll Stored Birthdays:")
# for name, dob in birthdays.items():
#     print(f"{name}: {dob}")
