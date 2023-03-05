from art import logo
import os

def add(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide,
}

def reset():
    os.system("clear")
    print(logo)


def calculate(previous_result):

    if previous_result == None:
        first_number = float(input("What's the first number? "))

    else:
        first_number = previous_result

    operation = ""

    while operation not in operations:
        operation = input("Pick an operation [+ - * /]: ")

        if operation not in operations:
            print("\nInvalid operation.")

    second_number = float(input("What's the next number? "))

    result = operations[operation](first_number, second_number)
    print(f"\n{first_number} {operation} {second_number} = {result}")

    return result


reset()
result = None
calculation_is_over = False

while not calculation_is_over:
    result = calculate(result)
    user_prompt = input(f"\nType 'y' to continue calculating with {result}, 'n' to begin a new calculation or anything else to exit: ")
    
    if user_prompt == 'n':
        result = None
        reset()
    
    elif user_prompt != 'y':
        calculation_is_over = True
