from tkinter import *
import random

# Initialize the main window
rps = Tk()
rps.geometry("300x300")  # Fixed typo "X" to "x"
rps.title("Rock Paper & Scissor")

# Initialize scores and choices
user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

# Mapping choices to numbers and vice versa
def choice_to_number(choice):
    rps = {'rock': 0, 'paper': 1, 'scissor': 2}
    return rps[choice]

def number_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissor'}
    return rps[number]

# Get a random computer choice
def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

# Determine the result
def result(human_choice, comp_choice):
    global user_score
    global comp_score
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    
    if user == comp:
        outcome = "Tie"
    elif (user - comp) % 3 == 1:
        outcome = "You win!!"
        user_score += 1
    else:
        outcome = "Computer Wins...!!"
        comp_score += 1

    # Display the result
    text_area = Text(master=rps, font=("arial", 15, "italic bold"), relief=RIDGE, bg="#033642", fg="white", width=26, height=5)
    text_area.grid(column=0, row=4)
    answer = f"Your choice: {human_choice}\nComputer's choice: {comp_choice}\nOutcome: {outcome}\nYour score: {user_score}\nComputer score: {comp_score}"
    text_area.delete(1.0, END)  # Clear the text area before inserting
    text_area.insert(END, answer)

# Define button actions
def rock():
    global user_choice
    global comp_choice
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def paper():
    global user_choice
    global comp_choice
    user_choice = "paper"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def scissor():
    global user_choice
    global comp_choice
    user_choice = "scissor"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

# Add buttons for user choices
button_rock = Button(text="   ROCK    ", bg="#808487", font=("arial", 15, "italic bold"), relief=RIDGE,
                     activebackground="#05945B", activeforeground="white", width=24, command=rock)
button_rock.grid(column=0, row=1)

button_paper = Button(text="   PAPER    ", bg="#808487", font=("arial", 15, "italic bold"), relief=RIDGE,
                      activebackground="#05945B", activeforeground="white", width=24, command=paper)
button_paper.grid(column=0, row=2)

button_scissor = Button(text="  SCISSOR   ", bg="#808487", font=("arial", 15, "italic bold"), relief=RIDGE,
                        activebackground="#05945B", activeforeground="white", width=24, command=scissor)
button_scissor.grid(column=0, row=3)

# Start the main loop
rps.mainloop()
