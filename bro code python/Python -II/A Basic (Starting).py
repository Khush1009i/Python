# First python program
print("I am Khush Soni")

#Variable = A container for a value, behaves as if it has the value it contains
# Variable - string, integer, float, boolean
# each variable must have a uniq name.


#String - are series of character, can be number, alphabets.
first_name = "Khush Soni"
food = "Daal Baati"
email = "sonikhush007@gmial.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your E-mail - {email}")

#Integers refers to quantity
age = 21 #don't use "" then it will become a string instead of a integer
quantity = 4
print("Your age",age)
print("You are buying", quantity, "items")


# Float = refers to floating number
price = 10.99
weight = 5.45
print(f"Your total is  {price} $")
print("Total weight is - ", weight, "Kg")


# Boolean (more used in if statements)
is_student = True 

for_sale = False

if for_sale:
    print("The item is yet for sale ")
else:
    print("The item is already sold")


print("You are a student at MLV Bhilwara",is_student)