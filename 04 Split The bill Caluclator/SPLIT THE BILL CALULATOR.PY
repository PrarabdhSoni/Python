print("Welcome to the split the bill calculator!😍")
bill = float(input("What was the total bill?\n₹ "))
tip = float(input("How much tip would you like to give?\n₹ "))
people = int(input("How many people to split the bill?\n"))
result = ((bill + tip)/people)
decimal= "{:.2f}".format(result)
print("Each person should pay🤑 :- ₹ " + decimal)