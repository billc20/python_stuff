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

#Write your code below this line 👇
import random
artwork = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if your_choice == computer_choice:
  print("Tie")
elif your_choice == 0:
  print(f"You chose: {rock}")
  if computer_choice == 1:
    print(f"Computer chose: {paper}")
    print("You Lose")
  elif computer_choice == 2:
    print(f"Computer chose: {scissors}")
    print("You Win")
elif your_choice == 1:
  print(f"You chose: {paper}")
  if computer_choice == 0:
    print(f"Computer chose: {rock}")
    print("You Win")
  elif computer_choice == 2:
    print(f"Computer chose: {scissors}")
    print("You Lose")
elif your_choice == 2:
  print(f"You chose: {scissors}")
  if computer_choice == 1:
    print(f"Computer chose: {paper}")
    print("You Win")
  elif computer_choice == 0:
    print(f"Computer chose: {rock}")
    print("You Lose")