from tkinter import *
import tkinter.messagebox

# Initialize the main Tkinter window
tk = Tk()
tk.title("Tic Tac Toe Multiplayer")

# Player Names
p1 = StringVar()
p2 = StringVar()

playerA = ""
playerB = ""

# Input fields for player names
Label(tk, text="Player 1 Name: ", font="Times 15 bold").grid(row=0, column=0)
player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=0, column=1)

Label(tk, text="Player 2 Name: ", font="Times 15 bold").grid(row=1, column=0)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=1, column=1)

# Game variables
bclick = True  # Toggle between players
flag = 0  # Track number of moves
buttons = []  # Store button references for iteration


def disableButton():
    """Disable all buttons once a win or tie occurs."""
    for btn in buttons:
        btn.configure(state=DISABLED)


def btnClick(button):
    """Handle button clicks."""
    global bclick, flag, playerA, playerB

    if button["text"] == " ":
        if bclick:
            button["text"] = "X"
            bclick = False
            playerA = p1.get() + " Wins!"
        else:
            button["text"] = "O"
            bclick = True
            playerB = p2.get() + " Wins!"
        flag += 1
        checkforwin()
    else:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Button already clicked!")


def checkforwin():
    """Check for a win or a tie."""
    global flag, playerA, playerB

    # Winning combinations
    win_combinations = [
        [button1, button2, button3],  # Row 1
        [button4, button5, button6],  # Row 2
        [button7, button8, button9],  # Row 3
        [button1, button4, button7],  # Column 1
        [button2, button5, button8],  # Column 2
        [button3, button6, button9],  # Column 3
        [button1, button5, button9],  # Diagonal 1
        [button3, button5, button7],  # Diagonal 2
    ]

    for combination in win_combinations:
        if combination[0]["text"] == combination[1]["text"] == combination[2]["text"] != " ":
            disableButton()
            if combination[0]["text"] == "X":
                tkinter.messagebox.showinfo("Tic Tac Toe", playerA)
            else:
                tkinter.messagebox.showinfo("Tic Tac Toe", playerB)
            return

    # Check for a tie
    if flag == 9:
        tkinter.messagebox.showinfo("Tic Tac Toe", "It's a Tie!")


# Create the game board buttons
button1 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)
buttons.append(button1)

button2 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)
buttons.append(button2)

button3 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)
buttons.append(button3)

button4 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)
buttons.append(button4)

button5 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)
buttons.append(button5)

button6 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)
buttons.append(button6)

button7 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)
buttons.append(button7)

button8 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)
buttons.append(button8)

button9 = Button(tk, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)
buttons.append(button9)

# Run the main loop
tk.mainloop()
