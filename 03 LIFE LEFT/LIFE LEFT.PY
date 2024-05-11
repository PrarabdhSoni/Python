age = (input("What is your current age? "))
age_int = int(age)

years_remaning = 100 - age_int
week_remaning = years_remaning * 52
months_remaning = years_remaning * 12
days_remaning = years_remaning * 365

result = f"You have {days_remaning} days, {week_remaning} weeks, and {months_remaning} months left."
print(result)