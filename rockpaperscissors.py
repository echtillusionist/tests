import random
import sys


def executeround():
    print("you are suddenly sucked into a game of rock paper scissors")

    options = [ "rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    player_choice = input("rock, paper, scissors, shoot -> (input your stance dummy)").lower()

    if player_choice not in options:
        print("thats not even a valid stance. try again. ")    
        return

    if (computer_choice == "rock" and player_choice == "scissors") or \
    (computer_choice == "paper" and player_choice == "rock") or \
    (computer_choice == "scissors" and player_choice == "paper"):
        print("lol get noob")
        print(f"i played {computer_choice}")
        playagain()

        
    elif computer_choice == player_choice:
        print("oh shit we tied dawg")
        print(f"i played {computer_choice} too")
        playagain()

    else: 
         print("well fuck me in the ass and call me patricia you won")
         playagain()

def playagain():
        redo = input("wanna play again? (yes/ no)").lower()
        if redo.lower() == "yes":
             executeround()
        elif redo.lower() == "no":
             print("peace")
             sys.exit()
        else:
             print("what are you doing you clown i asked a simple question")
             return

executeround()
