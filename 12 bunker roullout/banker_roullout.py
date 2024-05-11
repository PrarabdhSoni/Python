
import random

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

number = len(names)
rand = random.randint(0,number - 1)
print(names[rand] + " is going to buy the meal today!")