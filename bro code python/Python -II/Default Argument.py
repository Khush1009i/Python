# Default arguments: a default value for certain parametes,
#        default is used when that argument is omitted make
#       your own funxn more flexible,reduces # of arguments
#             1.Postional, 2.Default, 3.Keyword, 4.arbitary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount)*(1 + tax)



# Keyword -------------------------------------------------#
# argumnets preceded by an identifier helps with readablilty
# order of argument doesn't matter
#   1.positional 2. default 3. keyword 4. arbitrary

def hello(greet, title,first,last):
    print(f"{greet} {title} {first} {last} \nNice to meet you.")

# hello("Hello", first="Khush", last="Soni",title="Mr")

# for x  in range(1,11):
#    print(x, end=" ")

#-------------------------------------------------------------#


# Phone num:

def get_phone(country,  first, last):
    return(f"+{country} {first}-{last}")


phone_num = get_phone(country=91,first=96801, last=54388)
# print(phone_num)

#------------------------------------------------------------#



# Arbitarary:
# *args     = allow to pass multiple non-key argumants.
# **kwargs  = allow to pass multiple keyword argumants.
#...............*unpacking operator....................                 
#      1.positional 2. default 3. keyword 4. arbitrary.

#*args:

def add(*nums):
    total = 0
    for arg in nums:
        total += arg
    return total

def display_name (*args):
    for arg in args:
        print(arg, end=" ")

# display_name("Dr.","Spongebob")



# **kwargs:
# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address( locality = "875 Bapu nagar", 
#                city     = "Bhilwara",
#                zipcode  = "311001",
#                state    = "Rajsthan",
#                country  = "India")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print( )

    # for value in kwargs.values():
    #     print(value, end=" ")

    if "apt"in kwargs: 
        print(f"{kwargs.get('apt')}")
#--------------------------------------#
    
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
        print(f"{kwargs.get('street')}")
#--------------------------------------#
    
    else:
        print(f"{kwargs.get('street')}")
#--------------------------------------#

    print(f"{kwargs.get('locality')} {kwargs.get('zipcode')},{kwargs.get('state')},{kwargs.get('city')}, {kwargs.get('country')}")

shipping_label("Dr.","Spongebob","Harold","squarepants",
                pobox    = "875- 1/2 purani haveli",
                street   = "P-&-T Chauraha",
                locality = "Bapu-nagar", 
                city     = "Bhilwara",
                zipcode  = "311001",
                state    = "Rajsthan",
                country  = "India" )              