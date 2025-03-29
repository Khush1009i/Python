# Number Guessing Game using python: 

import random

low = 1
high = 50
ans = random.randint(low, high)

guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Slect the number between {low} and {high}: ")

while is_running:

    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if low < guess > high:
            print("That num is out of range...!")
            print(f"Please slect the number between {low} and {high}: ")
        elif guess < ans:
            print("Too Low...! Try again")
        elif guess > ans:
            print("Too High...! Try again")
        else:
            print(f"Correct answer: {ans}...!")
            print(f"num of guesses: {guesses}")
            is_running = False
    else:
        print("Invalaid guess")
        print(f"Please slect the number between {low} and {high}: ")