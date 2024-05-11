print("Welcome to Rollercoaster! 🎢")
height = float(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the Rollercoaster!😊")
    age = int(input("What is Your age?\n"))
    if age <= 10:
        bill = 50
        print("Child tickets are ₹50")
    elif age >10 and age <= 18:
        bill = 70
        print("Your tickets are ₹70")
    else:
        bill = 100
        print("Adult tickets are ₹100")
    wants_photo = (input("Do you want a photo taken? Y or N.\n")).lower()
    if wants_photo == "y":
        bill +=3
        print(f"your total bill is ₹{bill}🙏")
    else:
        print(f"Your total bill is ₹{bill}🙏")
else:
    print("Sorry, you have to grow taller before you can ride.☹️")