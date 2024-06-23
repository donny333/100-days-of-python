import os

def clear():
    """Clears all console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

#Calculator
    
#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    clear()
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calculations = input(f"Type 'y' to continue calculating with {answer}, type 'n' start a new calculation, or type 'e' to exit.: ")
        if continue_calculations == 'y':
            num1 = answer
        elif continue_calculations == 'n':
            should_continue = False
            calculator()
        else:
            return

calculator()