#from art import logo

#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2
  
#Multiply
def multiply(n1, n2):
    return n1 * n2
  
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
#print(logo)


def calculator():
    num1 = float(input("What is the first number?: "))
    
    
    for opt in operations:
      print(opt)
    
    continue_calc = True
    
    while continue_calc:
        operation_symbol = input("Pick an operation: ")
        
        num2 = float(input("What is the next number?: "))
        
        answer = operations[operation_symbol](num1,num2)
    
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        continue_option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'x' to exit: ")
        if continue_option == 'y':
            num1 = answer
        elif continue_option == 'n':
            calculator()
        else:
            continue_calc = False

calculator()
    
