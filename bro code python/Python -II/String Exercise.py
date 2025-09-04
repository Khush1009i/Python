# string - it's a series of characters.

name = input("Enter your fullname: ")
phone_number = input("Enter your phone number: ")

print(len(name))         # it defines the full length of the string.
print(name.find("h"))    # finds whaterver you put in.
print(name.rfind("i"))   # finds whaterver you put in from reverse.
print(name.capitalize()) # capatalize the first word.
print(name.upper())      # capatalize the word stored in. 
print(name.lower())      # capatalize the word stored in.
print(name.isdigit())    # returns true/false if only digi contains in the string.
print(name.isalpha())    # returns true/false if only aplhabet contains in the string(no space or num).

print(phone_number.count(" ")) #counts what you put in b/w ""
print(phone_number.replace("9", "0"))



# exercise# Validate user inout exercise
# 1.Username not more than 12 character
# 2.Username not contain spaces
# 3.Username not contain digit

username = input("Enter your user - name: ")

if len(username) >12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain space")
elif not username.isalpha(): 
    print("Your username can't contain any digits")
else:
    print(f"Welcome {username}\nHave good day sir ")