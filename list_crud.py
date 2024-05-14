try:
    #Create fruits list first
    fruitsList = []

    def add(fruitName):
        fruitsList.append(fruitName)
        print(f" {fruitName} added in Fruits List",fruitsList)
    
    def sortList(order = ""):
        if order == "ASC":
            fruitsList.sort()
            print(f" Fruitlist Sorted Assending order",fruitsList)
        elif order == "DESC":
            fruitsList.reverse()
            print(f" Fruitlist Sorted Desending order",fruitsList)
        else:
            print("Please secify sort order")

    def delete(name = ""):
        if name in fruitsList:
            fruitsList.remove(name)
            print(f" {name} removed from list",fruitsList)
        else: 
            fruitsList.pop()
            print(f"Last element removed from list",fruitsList)

    def getCount():
        print("Fruit List count is : ",len(fruitsList))
        
    add('Mango')
    add('Apple')
    sortList('ASC')
    sortList('DESC')
    delete("Mango")
    getCount()
except:
    print("Opps! Somthing went wrong...")