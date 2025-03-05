# conditional statements:
# if-elif-else

str = "I am going to learn a car"
print(str)

age = int(input("Enter your age = "))
if(age >= 18 ):
    print("Can vote & can apply for license")
elif(age <= 18):
    print("You have to wait, till 18!!")
else:
   print("Sorry, You can't")

light = input("enter the color of light = ")
if(light == "red"):
    print("you can't go further")
elif(light == "yellow"):
    print("You can start your car;s engine!")
elif(light == "green"):
    print("You can go now!")
else:
   print("Sorry, light is broken!")

marks = int(input("Enter your marks = "))
if(marks >= 90):
    print("You've 'A' grade")
elif(90 > marks >= 80):
    print("You've 'B' grade")
elif(80 > marks >= 70  ):
    print("You've 'C' grade")
    print("You've to work on yourself!")
elif(70 > marks >= 60):
    print("You've 'D' grade")
    print("Bring your parents next day ")
else:
    print("Meet me in Staff's room! ")