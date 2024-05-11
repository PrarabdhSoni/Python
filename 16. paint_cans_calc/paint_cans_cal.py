import math

def paint(height, width, coverage):
    num_cans = (height * width)/ coverage
    round_up_cans = math.ceil(num_cans)
    print(f"you will need {round_up_cans} cans of paint")

paint(50, 60, 10)