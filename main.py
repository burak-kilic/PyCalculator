from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    continuous = True
    while continuous:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's next number?: "))

        if operation_symbol in operations:
            func = operations[operation_symbol]
            answer = func(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            print("Invalid Operation")

        ans = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.\nType 'exit' to exit. : ").lower()

        if ans == "y":
            num1 = answer
        elif ans == "n":
            continuous = False
            calculator()
        elif ans == "exit":
            break


calculator()
