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


def calculator():
    num1 = int(input("What is the first number?"))

    6

    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:
        operation_choice = input("Pick an operation: ")
        num2 = int(input("What is the next number?"))
        calculation_function = operations[operation_choice]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_choice}{num2} = {answer}")
        
        if input(f"type y to continue calculating with {answer} or type n toexit") == "y":
            num1 = answer
        else:
            should_continue = False
            
        
        






    operation_choice = input("Pick another operation")
    num3 = int(input("What is your next number?"))

    second_answer= calculation_function(answer(num1, num2), num3)
    print(f"{answer} {operation_choice}{num3} = {second_answer}")
    
calculator()