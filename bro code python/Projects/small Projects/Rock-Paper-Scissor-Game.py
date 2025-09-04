# Rock Paper Scissor Game:



import random

player_name  = "Khush" #input("Enter player name: ") # assigning name 

option = ("rock","paper","scissors")

running = True

while running:
    player_choice = None
    computer_choice = random.choice(option)


    while player_choice not in option:
        player_choice = input("Enter a choice(Rock,Paper,Scissors): ")

    print(f"{player_name}: {player_choice}")
    print(f"Computer's:{computer_choice}" )

    if player_choice == computer_choice:
        print("It's a tie...")
    elif player_choice == "rock" and computer_choice == "scissors":
        print(f"{player_name} Wins...!")
    elif player_choice == "paper" and computer_choice == "rock":
        print(f"{player_name} Wins...!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print(f"{player_name} Wins...!")
    else: 
        print("You lose...!")

    if not input("Play Again? (Y / N)").lower() == "y":
        running = False

print("Thanks for playing")