# INPUT SECTION 
height = float(input("enter your height in m:\n"))
weight = float(input("enter your weight in kg:\n"))

# BMI FORMULA
BMI = (weight/(height ** 2))
print(BMI)
result = str(int(BMI))
print("Your BMI is " + result)

# IF ELSE STATEMENT 
if BMI>=18.5 and BMI<25:
 print("Congratulation you are normal 😊")
elif BMI<18.5:
  print("You are underweight 😊😉")
elif BMI>=25 and BMI<30:
  print("You are overweight.\nWork Hard 🏃")
elif BMI>=30 and BMI<=35:
  print("You are obese.\nWork Hard 🏃")
else:
  print("You are clinically obese.☹️")
