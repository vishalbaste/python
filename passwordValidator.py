import re
try:
    password        = input("Enter password : ")
    numberPattern   = r'[0-9]';
    capitalPattern  = r'[A-Z]';
    lowercasePattern= r'[a-z]';
    specialPattern  = r'[!@#$%^&*()_><?~{};*-]';

    if re.search(numberPattern, password) and re.search(capitalPattern, password) and re.search(lowercasePattern, password) and re.search(specialPattern, password) and 8 <= len(password) <= 16:
        print("Password is Valid")
    else:
        if not re.search(numberPattern, password):
            print("Password must contain at least 1 numeric character")
        if not re.search(capitalPattern, password):
            print("Password must contain at least 1 capital letter")
        if not re.search(lowercasePattern, password):
            print("Password must contain at least 1 small letter")
        if not re.search(specialPattern, password):
            print("Password must contain at least 1 special character")
        if not (8 <= len(password) <= 16):
            print("Password must be 8 to 16 characters")
except:
    print("Opps! somthing went wrong")