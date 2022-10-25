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


while True:
    import random

    try:
        game_images = [rock, paper, scissors]

        user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, 2 for Scissors.\n\n"))

        if user_choice >= 3 or user_choice < 0:
            print("Invalid value. Try again:")
        else:
            print(game_images[user_choice])

            computer_choice = random.randint(0, 2)
            print(f"Computer chose {computer_choice}")
            print(game_images[computer_choice])

            if user_choice == 0 and computer_choice == 2:
                print("You won!")
            elif computer_choice == 0 and user_choice == 2:
                print("You lost!")
            elif computer_choice > user_choice:
                print("You lost!")
            elif user_choice > computer_choice:
                print("You won!")
            elif user_choice == computer_choice:
                print("Its a Draw")

            play_again = input("Play Again? (y/n): ")
            if play_again.lower() != "y":
                print("Game ended")
                break

    except ValueError:
        print("Invalid Value")

