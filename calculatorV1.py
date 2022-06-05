#Functions Section
def addition(num1, num2):
    return num1 + num2

def soustraction(num1, num2):
    return num1 - num2

def division(num1, num2):
    return num1 / num2

def multiplication(num1, num2):
    return num1 * num2

#Main Section
while True:
    print("1: addition \n2: soustraction \n3: division \n4: multiplication")

    UserSelect = int(input())

    number1 = int(input())
    number2 = int(input())

    if UserSelect == 1:
        print(addition(number1, number2))
    elif UserSelect == 2:
        print(soustraction(number1, number2))
    elif UserSelect == 3:
        print(division(number1, number2))
    elif UserSelect == 4:
        print(multiplication(number1, number2))
    else:
        print("Invalid input, please try again") 
