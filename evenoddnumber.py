try:
    inputNumber = int(input("Please Enter Number: "));
    
    if ((inputNumber % 2) == 0):
        print(f" {inputNumber} is Even")
    else:
        print(f" {inputNumber} is Odd")
except:
    print("Please Enter Valid Number")