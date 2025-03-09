#-------------------------------------------------------------------------------------------------------------------#
# Q1.Write a program to input 2 numbers & print their sum:

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
sum   = a + b
diff  = a - b
multi = a * b 
divi  = a / b
mod   = a % b
print(a)
print(b)
print("addition = ",sum)
print("difference = ",diff)
print("multiply = ",multi)
print("divide = ",divi)
print("mode of = ",mod)
#-------------------------------------------------------------------------------------------------------------------#


# Q2.write a program to input side of a square & print its area:
length = int(input("Enter the lengeth of side of square:"))
print(length)
area = area = length ** 2
print("Area of a square: ",area)
#-------------------------------------------------------------------------------------------------------------------#


#Q3.Write a program to input 2 floating number & print thier average:
flo1 = float(input("enter the value 1:"))
flo2 = float(input("enter the value 2:"))
avg=(flo1 + flo2) / 2
print("average of two values is:",avg )
#-------------------------------------------------------------------------------------------------------------------#


# Q4.W.A.P to i/p num a & b. Print true if a >= b, if not print false:
a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
print(a >= b)

#-------------------------------------------------------------------------------------------------------------------#

# Q5. WAP to i/p user's first name & print its length.
name = input("Enter your name = ")
print(name)
print("Length of your name = ",len(name))
#-------------------------------------------------------------------------------------------------------------------#


# Q6. W.A.P. to find the occourance of $ in a string:
str = "I have atleast 100,000$ in my bank account."
print(str.count("$"))
#-------------------------------------------------------------------------------------------------------------------#


# Q7.WAP to check if number entered by the user is odd or even:
number = int(input("Enter the number: "))
if(number % 2 == 0):
    print("number is EVEN ")
else:
    print("Number is ODD")
#-------------------------------------------------------------------------------------------------------------------#


# Q8. WAP to find the greatest of 3 number enetered by the user:
a = int(input("enter th evalue of a:"))
b = int(input("enter th evalue of b:"))
c = int(input("enter th evalue of c:"))
if(a >= b and a >= c):
    print("a is the biggest number\n b is the second greatest number")
elif(b >= c and a >= c):
    print("b is greatest\n second is a")
else:
    print("c is greatest")
#-------------------------------------------------------------------------------------------------------------------#

# Q9. WAP to checck if a number is a multiple of 7 or not:
if(number % 7 == 0):
    print("it's a multiple of 7 ")
else:
    print("It's not!")
#-------------------------------------------------------------------------------------------------------------------#


# Q12. WAP to count num of students with the "A" grade in the following tuple:tup = ["C","D","A","A","B","B","A"]:
tup = ["C", "D", "A", "A", "B", "B", "A"]
print(tup.count("A"))
#-------------------------------------------------------------------------------------------------------------------#


# Q13.Store the above values in a list & sort them from "A" to "D"
list = tup
print("the new list is  = ",list)
list.sort()
print("The sorted list is  = ",list)
#-------------------------------------------------------------------------------------------------------------------#


# Q14. Store following word meaning in dictionary : a)table: "a piece of furniture","list of facts & figure"
# cat: "a small animal"
collection = {
    "table" : ["a piece of furniture", "list of facts & figure"],
    "cat"   : "a small animal"
}
#-------------------------------------------------------------------------------------------------------------------#


# Q15. U have given a list of subjects of students.Assume one classroom is require for subject. How many classroomm
# are needed by all students "python", "java", "C++", "python", "javascript", "java", "python", "C++", "C"
subject = {"python", "java", "C++", "python", "javascript", "java", "python", "C++", "C"}
print(type(subject))
print(subject)
print("Num of classroom needed: ",len(subject))
#-------------------------------------------------------------------------------------------------------------------#


# Q16. WAP to enter marks of 3 subjects from user & store them in a dict. Start with an empty & add one by one.
# Use subject names as keys & marks as value.
subjects ={}

x = int(input("enter your physics marks: "))
subjects.update({"phy": x})
##
y = int(input("enter your maths marks: "))
subjects.update({"maths": y})
##
z = int(input("enter your chemistry marks: "))
subjects.update({"chem": z})

print(subjects)
#-------------------------------------------------------------------------------------------------------------------#


# Q17.Print number from 1 t0 100.
i = 1
while i <= 100:
    print(i)
    i += 1 
#-------------------------------------------------------------------------------------------------------------------#


# Q18.Print number from 100 t0 1.
j = 100
while j >= 1:
    print(j)
    j -= 1
#-------------------------------------------------------------------------------------------------------------------#


# Q19.Print the multiplication table of a number n.
n = int(input("Enter the number: "))
m = 1
while m <= 10:
    print(n, "X" ,m, "=", n*m)
    m += 1
#-------------------------------------------------------------------------------------------------------------------#


# Q20.print the elements of the following list using a loop:
# n ==  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
#-------------------------------------------------------------------------------------------------------------------#

# Q21. Search for a number X in this tuple using loop: nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums =(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(nums)
i = 0
x = int(input("Enter your number:"))
while i< len(nums):
    if(nums[i] == x):
        print("FOUND @ : ", i)
    else:
        print("SORRY, NOT FOUND!")
    i += 1
#-------------------------------------------------------------------------------------------------------------------#


# Q22.Print element of following list using a loop:
n =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

n =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in n:
    print(val)
#-------------------------------------------------------------------------------------------------------------------#


# Q23.Search a number X in this tuple using loop: n =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("This is the tuple in data: ",n)
idx = 0
x = int(input("enter the number you want to find: "))
for char in n:
    if(char == x):
        print("Found",x, "at ",idx)
        break
    idx += 1
else:
    print("There is no element like",x,"in the tuple")
    print("Not found in it ...")
#-------------------------------------------------------------------------------------------------------------------#


#Using range:
# Q24. Print numbers from 1 to 100
# Q25. Print numbers from 100 to 1
# Q26. Print multi table of a num
for i in range(1,101): # 1 to 100
    print(i)

for j in range(100,0,-1): # 100 to 1
    print(j)

a = int(input("enter the table number: "))
for i in range(1,11): # mutip of num 
    print(a, "X", i, "=", a * i)
#-------------------------------------------------------------------------------------------------------------------#


# Q27.WAP to find sum of first n numbers (using while).
sum = 0
n   = int(input("enter the value of n: "))
i   = 1
while i <= n:
    sum += i
    i += 1
print("TOTAL SUM = ",sum)
#-------------------------------------------------------------------------------------------------------------------#


# Q28.WAP to find facctorial (using for)
n = int(input("enter the number: "))
fact = 1
# i =1

for i in range(1,n+1):
    fact *= i
print("Factorial: ",fact)
#-------------------------------------------------------------------------------------------------------------------#


# Q29.WAP to print length of a list
khush =[1,2,3,4,5,5]
villans = ["Voldmart","Homelander","Kira"]

def print_length(list):
    print(len(list))

def print_length(list):
    for it in list:
        print(it, end = "")
#-------------------------------------------------------------------------------------------------------------------#


# Q30.WAP to print element of a list in a single line.
khush =[1,2,3,4,5,5]
print(khush)

def print_length(list):
    print(len(list))

def print_length(list):
    for it in list:
        print(it, end = "")
#-------------------------------------------------------------------------------------------------------------------#


# Q31.WAP to find a factorial of n.
def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(4)
#-------------------------------------------------------------------------------------------------------------------#


# Q32. WAP to covert USD to INR ( 1$ = 86.5 ₹/-).
inr = 86.5
x = int(input("enter you $ "))
usd =  x * inr 
print("You have ",usd,"₹.")

y = int(input("Enter ₹ you have:  "))
dollor = 81
indian_rupee = y/dollor
print("you have ",indian_rupee,"$")

def convertor(usd_va):
    inr_val = usd_va * 86.5
    print(usd_va,"usd = ",inr_val,"INR")
convertor(12)
#-------------------------------------------------------------------------------------------------------------------#


# Q33. Write a recurrsive function to cal sum of first natural n number.
def cal_sum(n):
    if(n ==0):
        return 0
    sum = cal_sum(n-1) + n
    return sum

print(cal_sum(5))
#------------------------------------------------------------------------------------------------------------------#


# Q34. print all elements in a list (hint: use list & indx as parameter).
def print_list(list, indx = 0):
    if(indx == len(list)):
        return
    print(list[indx])
    print_list(list, indx+1)

fruits = ["mango", "apple", "banana"]
print_list(fruits)
#-------------------------------------------------------------------------------------------------------------------#


# Q35. create a new file "practice.txt" using python.
f = open("practise.txt","w") 
f.write("Hi everyone.\n we are learning I/O\n using java\n I like programming in java")
f.close()
print()
#-------------------------------------------------------------------------------------------------------------------#


# Q36. WAF taht replace all occurance of "java" with "python" in above file.
with open("practise.txt", "r") as f:
    data = f.read()

new_data = data.replace("java","python")
print(data)
#-------------------------------------------------------------------------------------------------------------------#


# Q36.Seaarch if the word "learning" exist in file or not.
def check_box():
    word = input("enter the word: ")
    with open("practise.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
          print("Found!. Your word: ",word)
        else:
            print("NOT FOUND!. Your word: ",word)
check_box()
#-------------------------------------------------------------------------------------------------------------------#


# Q37. WAf to find in which line does the word lerning occur first. Print-1 if word not found.       
def check_for_line():
    word = input("Enter the word: ")
    line_no = 1
    with open("practise.txt", "r") as f:
        for line in f:
            if word in line:
                print(line_no)
                return
                line_no += 1
            else:
                print("Not Found")
                break
           
    return -1

check_for_line()
#-------------------------------------------------------------------------------------------------------------------#


# Q38. Create a student class that takes name & marks of 3 subjects as arguments in constructor, 
#      then create a method to print the average:
class Students:

    def __init__(self,name, marks):
        s1.name = name
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name, "Your avg marks are :", sum/3)

s1 = Students("tony",[90, 91, 92])
s1.get_avg()
#-------------------------------------------------------------------------------------------------------------------#


# Q39 Define a Circle class to create a circle with radius r using constr. Define an Area() met of class with cal area of circle
# Define a Perimeter() met of class allw to cal perimeter 
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius ** 2
    
    def Perimeter(self):
        return 2 * (22/7)  * self.radius
    
c1  = Circle(21)
print(c1.Area())
print(c1.Perimeter())
#-------------------------------------------------------------------------------------------------------------------#


# Q40. Define a employee class with attr role , dept  & salary this class also have a showDetails() method.
#  Create an engineer class taht inherit prop from employee & 
class Employee:
    def __init__(self, role, dept, slry):
        self.role = role
        self.dept = dept
        self.slry = slry
        
    def showDetails(self):
       print("Role: ",self.role)
       print("Department: ",self.dept)
       print("salary: ",self.slry)
     
class Engineer(Employee):
    def __init__(self,name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Testing", "75000$")
    def showDetails(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        return super().showDetails()

E2 = Engineer("Khush Soni", 23)
E2.showDetails()
#-------------------------------------------------------------------------------------------------------------------#


# Q41.From a file containing num seprated by comma. print the count of even number

count =0
with open("practise.txt", "r") as f:
        data = f.read()
        print(data)

        num = ""
        for i in range(len(data)):
            if (data[i] == ","):
                print(int(num))
                num = ""
            else:
                num += data[i]   
                break     
             
nums = data.split(",") 
for val in nums:
     if(int(val)%2 == 0):
        count += 1
print(count)

# count_the_number()
#-------------------------------------------------------------------------------------------------------------------#