import random


def random_game():
    options = ["rock","paper","scissor"]
    while True:
        user_input = input("Choose one:\n1.Rock, 2.Paper, 3.Scissor")
        if(user_input.isdigit()):
            if int(user_input) > 3:
                print("Invalid input please type valid input")
                continue
            else:
                computer_choice = random.choice(options)
                player_choice = options[int(user_input)-1]
                
                if(computer_choice == "rock" and player_choice == "paper"):
                    print("User win")
                elif computer_choice == "paper" and player_choice == "scissor":
                    print("User win")
                elif computer_choice == "sciccor" and player_choice == "rock":
                    print("User win")
                else:
                    print("Computer win2")
                break



