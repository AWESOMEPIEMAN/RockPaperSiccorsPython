import random

comp_wins = 0
player_wins = 0


def human_choice():
    hchoice = input("Choose Rock, Paper or Scissors: ")
    if hchoice in ["Rock", "rock", "r", "R"]:
        hchoice = "r"
    elif hchoice in ["Paper", "paper", "p", "P"]:
        hchoice = "p"
    elif hchoice in ["Scissors", "scissors", "s", "S"]:
        hchoice = "s"
    else:
        print("I don't understand, try again.")
        human_choice()
    return hchoice


def comp_choice():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")

    user_choice = human_choice()
    comp_choice = comp_choice()

    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied.")

        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1

        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            player_wins += 1

        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You tied.")


        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1

        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            player_wins += 1

        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
