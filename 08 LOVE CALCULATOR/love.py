
print("Welcome to the Love Calculator!❤️")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
Name = name.lower()
t = int(Name.count("t"))
r = int(Name.count("r"))
u = int(Name.count("u"))
e = int(Name.count("e"))
true = str(t + r + u + e)

l = int(Name.count("l"))
o = int(Name.count("o"))
v = int(Name.count("v"))
e = int(Name.count("e"))
love = str(l + o + v + e)

total = int(true + love)
if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.💣")
elif total>=10 and total<50:
    print(f"Your score is {total}, you are alright together.❤️")
else:
    print(f"Your score is {total}.😍")