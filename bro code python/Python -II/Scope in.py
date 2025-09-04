# Scope in python  = Global and Local
# variable scope   = where a variable is visible & accesible
# scope resolution = Local-> enclosed-> Global-> Built-in


# x =3
# def func1():
#     print(x)
    
#     def func2():
#         print(x)
#     func2()


# func1()


from math import e

def func1():
    print(e)

func1()
