# Inheritence & Polymorphism:
#del keyword : used to delete obj prop or obj itself.
class Student:
    def __init__(self, name ):
        self.name = name
        print(self.name)    
# s1 = Student("Khush")
# print(s1.name)
# del s1.name
# --> print(s1.name) #It will not print anything.
# Just say that there is no attribute name in Student


# Private(like) attribute & methods:
# used only 


class Account:
    def __init__(self, acc_no, __acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = __acc_pass
 # "__ "this'll make it privete
    def reset_pass (self):
        print("Account passkey:",self.__acc_pass)
    # it accessible in class but not out of the class.
    # out of the class it will never return value.

# acc1 = Account("135213", "abdfhj")
# print("Account number: ",acc1.acc_no) 
# # print(acc1.__acc_pass)    
# print(acc1.reset_pass())


class Person:
    __name = "Khush"
    # print(__name)
  
    def __hello(self):
        print("Hello !")
    
    def welcome(self):
       self.__hello()

p1 = Person()
# print(p1.__name)
# print(p1.__hello())
# print(p1.welcome())

# Inheritence:
#oneclass(childerived) derives prop & methods of another class

class Car:
    @staticmethod
    def start():
        print("Car Started")
    def stop():
        print("Stop Car")

    def __init__(self, color, company):
        self.color = color
        self.company = company
s1 = Car("Blue","Toyota")

#Single Inheritence
class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand
car1 = Toyota("Fortuner")
car2 = Toyota("Sorto")
# print(car1.name)
# print(car1.start())

# Types of Inheritence:
# -->Single Inheritence
# -->Multi-level
# -->Multiple

#Multi-level Inheritance:
class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type
        print("Car type: ",self.type)

class Supra(Toyota):
    def __init__(self, type):
        self.type = type
        print(self.type)

# car1 = Fortuner("Diesel")
# car1 = Supra("Petrol -Turbo")
# car1.start()
# car2.start()

# Multiple class inheritence:

# class A:
#     varA = "Welcome to class A"
# class B(A):
#     varB = "Welcome to class B"
# class C(A,B):
#     varC = "Welcome to class A"
# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# Super Method:
class Car:
     def __init__(self, type):
        self.type = type

     @staticmethod
     def start():
         print("Car Started")
     @staticmethod
     def stop():
         print("Stop Car")

class Toyota(Car):
    def __init__(self, name, type):
        super().__init__(type) # Super constructor
        self.name = name
        # super().start()

car1 = Toyota("Fortuner","electric")
# print("Car name:",car1.name)
# print("Car type:",car1.type)


# Class Method: bound to class & recieves class as an implicit first argument.
# Note:- static met can't access or modify class state & generally for utility.

class Person:
    name  = "Khush Soni"
    
    # def change_name(self, name): # self == object
    #     # self.name = name
    #     self.__class__.name = "Khush"

    @classmethod # decorator
    def change_name(cls,name):
        cls.name = name

# p1 = Person()
# p1.change_name("Khush")
# print(p1.name)
# print(Person.name)


# Type of Methods:
# --> static Methods.
# --> class Methods.
# --> Insatnce Methods.

# Property: use @property deco on any method 
# in class to use method as a property

class College:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        
    
    #def cal_percentage (self):
    # self.percent =str((self.chem+ self.maths+ self.phy)/3)+ "%"
   
   
    @property  #decorator
    def percent(self):
        return str((self.chem+ self.maths+ self.phy)/3)+ "%"
stud1 = College(56, 76, 67)

stud1.phy = 86
# print( stud1.phy) 

# print(stud1.percent)



#------------------------------------------------------------#

# Polymorphism : Operator overloading
#when same oprtr is allwd to hve differ means acc to cntxt.

# print(1+2, type) # 3
# print("Khush " + "Soni",type) #concatenate
# print([1,2,3] + [4,5,6], type) #merge
 
class Complex:
    def __init__(self, real, imagi):
        self.real = real
        self.imagi = imagi
    def show_number(self):
        print(self.real,"i + ",self.imagi,"j")

# num1 = Complex(1,2)
# num1.show_number()
# num2 = Complex(12,22)
# num2.show_number()


#|Operators         &     Dunder       |
#|------------------|------------------|
#|a + b: additon    |a.__add__(b)      |
#|a - b: subtract   |a.__sub__(b)      |
#|a * b: multiply   |a.__mul____(b)    |
#|a / b: division   |a.__truediv____(b)|
#|a % b: addition   |a.__mod____(b)    |
#|------------------|------------------|

class Complex:
    def __init__(self, real, imagi):
        self.real = real
        self.imagi = imagi

    def show_number(self):
        print(self.real, "i + ", self.imagi, "j")

    def __add__(self, num2):
        new_real = self.real + num2.real
        new_img = self.imagi + num2.imagi
        return Complex(new_real, new_img)

    def __sub__(self, num2):
        new_real = self.real - num2.real
        new_img = self.imagi - num2.imagi
        return Complex(new_real, new_img)

    def __mul__(self, num2):
        new_real = self.real * num2.real - self.imagi * num2.imagi
        new_img = self.real * num2.imagi + self.imagi * num2.real
        return Complex(new_real, new_img)

    def __truediv__(self, num2):
        r = num2.real ** 2 + num2.imagi ** 2
        new_real = (self.real * num2.real + self.imagi * num2.imagi) / r
        new_img = (self.imagi * num2.real - self.real * num2.imagi) / r
        return Complex(new_real, new_img)

    def __mod__(self, num2):
        # Note: modulus operation is not well-defined for complex numbers
        # You may want to implement a different operation, such as magnitude
        pass



# num1 = Complex(1,3)
# num1.show_number()

# num2 = Complex(4, 6)
# num2.show_number()

# # num3 = num1.add(num2) if we don't define method as dunder 
# num3 = num1 + num2
# num3.show_number()

# # num1.sub(num2)
# num4 = num1 - num2
# num4.show_number() 

# num5 = num1 * num2
# num5.show_number()

# num6 = num1 / num2
# num6.show_number()


