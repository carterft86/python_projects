import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game_images = [rock, paper, scissors]

your_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(f"Your choice: {your_choice}")
print(game_images[your_choice])

computer_choice = random.randint(0, 2)
print(f"Computer's choice: {computer_choice}")
print(game_images[computer_choice])

if your_choice >= 3 or your_choice < 0:
    print("You have entered invalid number. You lost.")
elif your_choice == 2 and computer_choice == 0:
    print("You lost")
elif computer_choice == 2 and your_choice == 0:
    print("You won!")
elif your_choice > computer_choice:
    print("You won!")
elif computer_choice > your_choice:
    print("You lost")
elif computer_choice == your_choice:
    print("Its a draw. Try it again!")
