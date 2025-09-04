# function = a block of reusable code.
#            place () after function name to invoke it


#  return =  statement used to end a function & send result
#              back to caller

def happy_bday(name, age):  # position of perimeters does matter.
     print(f"Happy bday  {name}...!!!!!")
     print(f"You are now {age} old...!!!!!!")


def display_invoice(username, amount, due_date):
     print(f"Hello {username}")
     print(f"Your bill of ${amount: .2f} is due: {due_date}")

# display_invoice("Khush",45, "07/06")


# Return: 
def add(x,y):
     z = x+y
     return z
def add(x,y):
     z = x+y
     return z

def subtract(x,y):
     z = x - y
     return z

def multiply(x,y):
     z = x * y
     return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))

def create_name(first, last):
     first = first.capitalize()
     last = last.capitalize()
     return first + " " +last
full = create_name("SPonebob","squarepants")
print(full)