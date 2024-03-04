def add(n1, n2):
    return n1+ n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What is the first number?"))


for operation in operations:
    print(operation)
    
operation_choice = input("Pick an operation from the line above: ")

num2 = int(input("What is the second number?"))

calculation_function = operations[operation_choice]
answer = calculation_function(num1, num2)