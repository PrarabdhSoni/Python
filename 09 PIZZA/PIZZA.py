print("Welcome to Pizza Deliveries!🚲")
bill = 0

# Pizza Names
pizza = ["1. Peppy Paneer = ₹459🍕\n", "2. Veggie Paradise = ₹459🍕\n", "3. Veg Loaded = ₹249🍕\n", "4. Panner and Capsicum = ₹249🍕\n", "5. Margherita = ₹149🍕\n", "6. Cheese n Corn = ₹149🍕\n"]
print(pizza[0])
print(pizza[1])
print(pizza[2])
print(pizza[3])
print(pizza[4])
print(pizza[5])

# order input
order = input("Which pizza you want to eat today🍕. For order just write Sr.No. just like if you want to order Peppy Paneer just type 1\n")
if order == "1" or order == "2":
    bill += 459
elif order == "3" or order == "4":
    bill += 249
elif order == "5" or order == "6":
    bill += 149
else:
   print("Please write Correct")


# aditional items
size = input("What size pizza do you want? S, M, or L\n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N\n").lower()
extra_cheese = input("Do you want extra cheese🧀? Y or N\n").lower()
coke = input("Did you want coke🥤? Y or N\n").lower()

# Selecting Size
if size == "s":
    bill += 50
elif size == "m":
    bill += 70
elif size == "l":
    bill += 100
else:
    print("Please write Correct")

# Add Pepperoni or not
if add_pepperoni == "y":
    if size == "s" or size == "m":
        bill += 20
    elif size == "l":
        bill += 30
else:
    bill += 0

# Extra cheese?
if extra_cheese == "y":
    bill += 25
else:
    bill += 0

# add coke ?
if coke == "y":
    bill += 60
elif coke == "n":
    bill += 0

#GST
GST = bill * .18
print(f"Your GST is ₹{GST}\n")
total = int(bill + GST)

# Final Bill 
print(f"Your final bill is: ₹{total}\n")

#User Information
address = input("Please provide your Address for dilivery\n")
contact_details = input("Please provide contact number\n")
contact = int(len(contact_details))

if contact == 10:
    print("Thanks for order!😊")
    print("Our delivery partner reach out to you soon!")
else:
    print("Please provide correct mobile number")