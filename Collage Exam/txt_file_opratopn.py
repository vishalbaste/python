def createFile(filename):
    file = open(filename,'w')
    print("file created successfully",format(filename))

def storeData(filename,data):
    file = open(filename,'a')
    file.write(data)
    print("Data Added")

def readLines(filename):
    file = open(filename,'r')
    lines = file.readlines()
    lineCount = len(lines)
    print(f"{filename} contains {lineCount} lines")

def getWordCount(filename):
    file = open(filename,'r')
    content = file.read()
    word = content.split()
    wordCount = len(word)
    print(f"{filename} contains {wordCount} words")

def readData(filename):
    file = open(filename,'r')
    content = file.read()
    print(f"{filename} data is : ",content)
# createFile('employee.txt')
# storeData('employee.txt','Hello World')
# readLines('employee.txt')
# getWordCount('employee.txt')
readData('employee.txt')