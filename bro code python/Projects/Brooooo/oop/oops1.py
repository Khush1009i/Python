# oops in python: 
a = 12
b = 34

sum = a + b
diff = b - a
div  = b/a
print("sum: ",sum)
print("diff: ", diff)
print("div:",div)

# Class & Object: 
# -- class is a blueprint for creting  a object.
 

#------------------------------------------------#

# init function:
class Student:
    college = "M.L.V. Textile & Engineering College,Bhl"
    # name = "anonymous"   -- class attr
    #default constructors:
    def __init__(self):
        print("Adding Students to database")

        #parameter constructor:
    def __init__(self, name,rollnum,dob):
        self.name = name # object attr
        self.rollnum = rollnum
        self.dob = dob


s1 = Student("Khush",24,"12-12-1994")

s2 = Student("Karan",23,"07-06-2004")
print("Student1 :",s1.name, s1.rollnum, s1.dob, s1.college)
s1.hello
print("Student2 :",s2.name, s2.rollnum, s2.dob, s2.college)


# Attributes: class & Instance are two types of attributes.
# obj attr >> class attr


# Methods:
class Car:
    def __init__(self,name):
        self.name = name
        
    def welcome(self):
        print("Welcome sir",self.name)

m1 = Car("BMW m8")
m1.welcome()


#--------------------------------------------#

# Static Method: there is no self parameter & it works at class leve
# decorater:it allow to wrap funx in order to extend 
# behaviour of wrapped funxn & without permnt modifying it.
class Students:

    def __init__ (self,name, marks):
        self.name = name
        self.marks = marks

    @staticmethod #decorater
    def hello():
        print("Nice to meet you")   
    @staticmethod #decorater &
    def College():
        print("M.L.V. Tectile & Engineering college,Bhl")


    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name, "Your avg marks are :", sum/3)


s1 = Students("tony",[90, 91, 92])
s1.get_avg()
s1.hello()
s1.College()


#Abstraction & Encapsulation:
# Abstraction: Hiding

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def Start(self):
        self.clutch = True
        self.acc = True
        print("car start...")

car1 = Car()
car1.Start()

# Encapsulation: wrapping data & fumxn into single unit.(object)

# Q39.Create a account class with 2 attr - balance & accno.
# Create methodes for debit credit & printing balance

class Bank:
    def __init__(self,bal, accno):
        self.balance = bal
        self.accno = accno

    def debit(self, amount):
        self.balance -= amount
        print("rs.",amount, "was debited")
        print("Your total balance: ", self.get_balance())
    
    def credit(self, cred):
        self.balance += cred
        print("Rs.",cred, "to your bank acc")
        print("Your total balance: ", self.get_balance())
    
    def get_balance(self):
        return self.balance


acc1 = Bank(10000, 133213)

acc1.debit(1000)
acc1.credit(345)