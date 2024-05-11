print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|__________________-_-:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.- 🪙🪙 `"=._o." ,-"""-._ ".   |
|___________________|_._"  🪙 🪙 🪙 🪙 `"-._"-._   ". '__|___________________
          |           |o`"=._🪙 🪙 🪙 🪙 🪙 "-._"-._; ;              |
 _________|___________| ;`-.o`"=._🪙 🪙 🪙 🪙 🪙 "_./ "_______________|_______
|                   | |o;    `"-.o`"=._🪙 🪙      _.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to treasure iland Game 🎮")
print("Your mission is to find the treasure.🪙")

go = input("You're at a cross road. Where do you want to go? Type left or right\n").lower()
if go == "left":
    print("Game over you fall in hole.☹️")
elif go == "right":
    print("Well Done! 👍")
    swim = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if swim == "swim":
       print("Game over you die ☹️")
    elif swim == "wait":
       print("Well done! keep it up😊")
       color = input("You arrive at the island unharmed. There is a house with 3 doors. One red🔴, one yellow🟡 and one blue🔵. Which colour do you choose?\n").lower()
       if color == "red":
           print("Game over you choose fire door🔥💀")
       elif color == "blue":
           print("Game over you choose dinosaur door 🦖💀")
       elif color == "yellow":
           print("You found the treasure! You Win!🪙🥳")
       else:
           print("Please type correct")
    else:
        print("Please type correct")
else:
    print("Please type correct")
    