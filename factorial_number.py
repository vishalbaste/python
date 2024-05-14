#Program to genrate factorial number
'''
    0! = 1
    1! - 1*1 = 1
    2! - 2*1 = 2
    3! - 3*2*1 = 6
    4! - 4*3*2*1 = 24
'''
try:
    inputNumber = int(input("Please Enter Number : "));
    factorial = 1
    if inputNumber > 0:
        for i in range(1,inputNumber+1):
            factorial = factorial * i
        print(f"{inputNumber}! is : {factorial}")
    elif inputNumber == 0:
        print(f"{inputNumber}! is : 0")
    else:
        print("Please enter positive number");
except: 
    print("Print Enter Valid Number");