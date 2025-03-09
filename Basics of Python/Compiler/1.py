import tkinter
from tkinter import *

root = Tk()
root.Title("Simple calculator")
root.geometry("570*600+100+200 ")
root.resizable(False,False)
root.configure(bg = "#171161b")

equation = ""
def show(value):
    global equation
    equation += value
    label_result.config(text = equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation
    result =""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
        label_result.config(text=result)


label_result = Label(root, width =25, height=2, text="", font=("arial",30))
label_result.pack()

Button(root, text="C", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda:clear()).palce(x=10,  y=100)
Button(root, text="/", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("/")).palce(x=150, y=100)
Button(root, text="*", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("*")).palce(x=290, y=100)
Button(root, text="%", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("%")).palce(x=430, y=100)

Button(root, text="7", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("7")).palce(x=430, y=100)
Button(root, text="8", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("8")).palce(x=430, y=100)
Button(root, text="9", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("9")).palce(x=430, y=100)
Button(root, text="-", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("-")).palce(x=430, y=100)

Button(root, text="6", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("6")).palce(x=430, y=100)
Button(root, text="5", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("5")).palce(x=430, y=100)
Button(root, text="4", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("4")).palce(x=430, y=100)
Button(root, text="+", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("+")).palce(x=430, y=100)

Button(root, text="3", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("3")).palce(x=430, y=100)
Button(root, text="2", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("2")).palce(x=430, y=100)
Button(root, text="1", width=5, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("1")).palce(x=430, y=100)
Button(root, text="0", width=11, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("0")).palce(x=10, y=100)


Button(root, text=".", width=11, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show(".")).palce(x=290, y=500)
Button(root, text="=", width=11, height= 1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:calculate()).palce(x=430, y=400)



root.mainloop()