# Functions in python 
# block of statements that perform a specific task.
# function is used for less redundancy.
def calSum(a, b):#parameters
    return a+b
sum = calSum(12,23)
print(sum)

sum = calSum(15, 45)
print(sum)

def print_hello():
    print("Hello world")

output = print_hello()
print(output)

def avg_num(a,b,c):
    sum = a+b+c
    average = sum/3
    print(average)
    return average

avg_num(98, 97, 95)

# #|Built-in function |
# #|print()           |
# #|len()             |
# #|type()            |
# #|range()           |


print("Khush soni","Gagan Soni")

def cal_prod(a=1,b=1):
    print(a * b)
    return a * b

cal_prod(1)

def number(a):
    while a:
        if(a % 2 == 0):
            print("EVEN")
            break
        else:
            print("ODD")
            break

number(10)
number(19)