#Calculator easyer program

def addition(num1, num2):
    return num1 + num2

def soustraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

#loop
while True:
    number_1 = int(input())
    UserSymbol = str(input())
    number_2 = int(input())

#Conditions
    if UserSymbol == "+":
        print(addition)
    elif UserSymbol == "-":
        print(soustraction)
    elif UserSymbol == "*":
        print(multiplication)
    elif UserSymbol == "/":
        print(division)
    else:
        print("Syntaxe error")
