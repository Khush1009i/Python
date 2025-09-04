from tkinter import *  # Importing tkinter modules
from tkinter import ttk
import tkinter.messagebox


def main():
    root = Tk()
    app = Windows1(root)  # Class name follows PascalCase convention
    root.mainloop()


class Windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry("1350x750+0+0")  # Corrected geometry string
        self.frame = Frame(self.master)
        self.frame.pack()

        self.labelTitle = Label(
            self.frame,
            text="Pharmacy Management System",
            font=("arial", 40, "bold"),
            bd=10,
            relief="sunken",
        )
        self.labelTitle.grid(row=0, column=0, pady=20)

        # Frames
        self.loginframe1 = Frame(self.frame, width=1000, height=300, bd=10, relief="groove")
        self.loginframe1.grid(row=1, column=0)

        self.loginframe2 = Frame(self.frame, width=1000, height=300, bd=10, relief="groove")
        self.loginframe2.grid(row=2, column=0, pady=15)

        self.loginframe3 = Frame(self.frame, width=1000, height=300, bd=10, relief="groove")
        self.loginframe3.grid(row=3, column=0, pady=5)

        self.button_reg = Button(self.loginframe3, text="PAtient Registration Window",font=("arial", 15,"bold"), command=self.Registration_window)
        self.button_reg.grid(row=0, column=0,padx=10, pady=10)

        self.button_Hosp = Button(self.loginframe3, text="PAtient Registration Window",font=("arial", 15,"bold"), command=self.Hospital_window)
        self.button_Hosp.grid(row=0, column=0,padx=10, pady=10)

        self.button_Dr_appt = Button(self.loginframe3, text="PAtient Registration Window",font=("arial", 15,"bold"), command=self.Dr_Appoint_window)
        self.button_Dr_appt.grid(row=0, column=0,padx=10, pady=10)

        self.button_med_stock = Button(self.loginframe3, text="PAtient Registration Window",font=("arial", 15,"bold"), command=self.Medicine_stock_window)
        self.button_med_stock.grid(row=0, column=0,padx=10, pady=10)


    # Methods for opening new windows
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows3(self.newWindow)

    def Dr_Appoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows4(self.newWindow)

    def Medicine_stock_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows5(self.newWindow)


class Windows2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Management System")
        self.master.geometry("1350x750+0+0")  # Corrected geometry string
        self.frame = Frame(self.master)
        self.frame.pack()


class Windows3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry("1350x750+0+0")  # Corrected geometry string
        self.frame = Frame(self.master)
        self.frame.pack()


class Windows4:
    def __init__(self, master):
        self.master = master
        self.master.title("Doctor Appointment System")
        self.master.geometry("1350x750+0+0")  # Corrected geometry string
        self.frame = Frame(self.master)
        self.frame.pack()


class Windows5:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine System")
        self.master.geometry("1350x750+0+0")  # Corrected geometry string
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == "__main__":
    main()
