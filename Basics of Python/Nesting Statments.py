# nesting

age = int(input("Enter your age =  "))
if(age >= 18):
    if(age >= 80):
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")