#while loop; executes some code WHILE, some condition remains True.


# name = (input("Enter your name: "))

# while name =="" :
#      print("You didn't type your name...!")
#      name = input("Enter your name: ")
# else:
#     print(f"Hola, Mr.{name}")


    
# print(f"You are {age} years old! As Fuck!!")

# age = int(input("Enter your age: "))

# while age < 0 :
#     print("Age can't be negative...!")
#     age = input("Enter your age: ")

# print(f"You are {age} years old! As Fuck!!")


# food = input("Enter a food you like( q to quit)")

# while not food == "q":
#     print(f"u like {food}")
#     food = input("Enter some another food u like (Q to quit ) ")


# print("Bye-Bye ")

num = int(input("Enter a # between 1 - 10: "))

while num <1 or num >10 :
    print(f"{num} is not valid!")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number was: {num}")