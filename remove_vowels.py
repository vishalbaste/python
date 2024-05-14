import re

#Vovels are a,e,i,o,u
#remove it using regulator expression

try:
    #take string from user
    stringInput = input("Enter string to remove vovels : ")
    #take capital and lowercase letter to remove from string
    pattern = r'[aeiouAEIOU]'

    outputString = re.sub(pattern,'',stringInput)

    print(f"Orignal string is : {stringInput} after removing vovels: {outputString}")
except:
    print("Opps! somthing went wrong")