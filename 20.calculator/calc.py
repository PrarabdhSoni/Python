import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 + n2
def multiply(n1,n2):
    return n1 * n2
def division(n1, n2):
    return n1/n2

operation ={
    "+": add,
    "-": sub,
    "*": multiply,
    "/": division,
}

def calculator():
    print(logo)
    num1 = float(input("What is your 1st number?\n"))

    should_continue = True

    while should_continue:
        for symbols in operation:
            print(symbols)
        operation_symbol = input("Choose one operations from above\n")

        num2 = float(input("What is your next number?\n"))

        calculation = operation[operation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("did you want to continue the calculation if yes type 'y' or type 'n' for new calculation\n").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            os.system("cls")
            calculator()


calculator()