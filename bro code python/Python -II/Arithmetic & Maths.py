# arithmetic & maths related material
import math


#friends = 2
# friends += 1 #add
# friends -= 2 #
# friends *= 4
# friends /= 2
# friends %=  2
# friends **= 2
# print("Num of friends you have- ",friends)
x = 3.14 
y = 4
z = 5
# result = round(x) 
#round is used to round-off any specific number 
# result = abs(y)
#abs makes the integer a absolute value
# result = pow(x,y) 
#pow gives us the power value of integer
# result1 = max(x,y,z) 
# result2 = min(x,y,z) 
# # max & min shows the min and max int
# print("e - ",math.e)
# print("pi - ",math.pi)
# result  = math.cbrt(1225)
# result = math.ceil(x) 
# # round-off with more 
# result = math.floor(y)
#  # round-off with less 
# print(result)

# radius = float(input("Enter the radius of circle - "))

# crcmfrnce = 2* math.pi * radius # circumference of a circle.
# area = math.pi * (radius**2) # Area of a circle.

# print("Circumference of the circle - ",round(crcmfrnce,1))
# print("Area of the circle - ",round(area,2))


# How to find hypotenuse of a traingle ?
# Solve --
 
a = float(input("Enter the value of A - "))
b = float(input("Enter the value of B - "))

c = math.sqrt(pow(a,2) + pow(b,2))

c = round(c)
print(f"Area of triangle is - {c}")