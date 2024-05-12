import re
try:
    pattern = r'\b[a-zA-Z0-9.]+@[a-zA-z0-9]+\.[A-Za-z]{2,7}\b'

    def checkEmail(email):
        if(re.match(pattern,email)):
            print(f"{email} is Valid")
        else:
            print(f"{email} is invalid")

    checkEmail('dev@gmail.com')
    checkEmail('dev@')
except:
    print("Opps! Somthing went wrong")