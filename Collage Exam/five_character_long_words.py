def getFiveLengthWord(line):
    lineArray = line.split(" ")
    matchArray = []
    for word in lineArray:
        if len(word) == 5:
            matchArray.append(word)

    return matchArray

fiveList = getFiveLengthWord("Hello world this is test line to scrap wrords")

print(fiveList)