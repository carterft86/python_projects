import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()
        print("Please type in rock, paper, or scissors")

    if player == computer:
        print("player: ", player)
        print("computer: ", computer)
        print("It's a tie")
    elif player == "rock":
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Good Bye!")
