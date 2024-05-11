
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

#Write your code below this line 👇
while True:
  user_input = int(input("What did you choose? Type 0 for rock ✊, 1 for paper ✋ or 2 for scissors ✌️.\n"))
  if user_input == 0:
    print(rock)
  elif user_input == 1:
    print(paper)
  elif user_input == 2:
    print(scissors)
  
  computer_choice = int(random.randint(0, 2))
  print(f"computer choice is {computer_choice}")

  if computer_choice == 0:
    print(rock)
  elif computer_choice == 1:
    print(paper)
  elif computer_choice == 2:
    print(scissors)
  
  if computer_choice == 0 and user_input == 1:
    print("You Wins!")
  elif computer_choice == 1 and user_input == 0:
    print("You Lose!")
  elif computer_choice == 0 and user_input == 2:
    print("You Lose!")
  elif computer_choice == 2 and user_input == 0:
    print("You Wins!")
  elif computer_choice == 1 and user_input == 2:
    print("You Wins!")
  elif computer_choice == 2 and user_input == 1:
    print("You Lose!")
  elif computer_choice == user_input:
    print("Tie")
  else:
    print("You typed invalid, You Lose!")
