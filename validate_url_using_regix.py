import re
try:
    pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}(/\S*)?$'

    def checkURL(url):
        if(re.fullmatch(pattern,url)):
            print(f"{url} is Valid URL")
        else:
            print(f"{url} is invalid URL")

    checkURL('example.com')
    checkURL('www.example.com')
    checkURL('example')
except:
    print("Opps! somthing went wrong")