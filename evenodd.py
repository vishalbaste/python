def checkNumber(number):
    if(number % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

try:
    inputNumber = int(input("Please enter number..."))
    checkNumber(inputNumber)
except ValueError:
    print("invalid number! please enter correct number")