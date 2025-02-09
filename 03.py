# Aim
# Build a calculator in Python that can perform basic arithmetic operations.

import random

def generateExpression():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)

    operators = ['+', '-', '*', '/']

    operator = random.choice(operators)

    if operator == '/' and operand2 == 0:
        operand2 = random.randint(1, 100)

    expression = f"{operand1}{operator}{operand2}"

    return expression

def getOperands(expression: str):
    i = 0
    firstOperand = ""
    operator = ""
    secondOperand = ""

    while i < len(expression) and expression[i].isdigit():
        firstOperand += expression[i]
        i += 1

    if i < len(expression) and not expression[i].isdigit():
        operator = expression[i]
        i += 1
    
    while i < len(expression) and expression[i].isdigit():
        secondOperand += expression[i]
        i += 1

    return firstOperand, operator, secondOperand

def calculate(firstOperand, operator, secondOperand):

    if (firstOperand == "" or operator == "" or secondOperand == ""): 
        print("Please correct the expression")
    else:
        firstOperand = float(firstOperand)
        secondOperand = float(secondOperand)
        if(operator == '+'):
            return firstOperand + secondOperand
        elif(operator == '-'):
            return firstOperand - secondOperand
        elif(operator == '*'):
            return firstOperand * secondOperand
        elif(operator == '/'):
            return firstOperand / secondOperand
        else:
            return "Didn't find any operator in the given expression."

expression = generateExpression()
print(expression)
firstOperand, operator, secondOperand = getOperands(expression)
print(calculate(firstOperand, operator, secondOperand))