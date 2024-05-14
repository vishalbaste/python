import threading

def printNum1(num):
    print(f"Number 1 is : {num}")

def printNum2(num):
    print(f"Number 2 is : {num}")

if __name__ == "__main__":
    t1 = threading.Thread(target=printNum1,args=(10,))
    t2 = threading.Thread(target=printNum2,args=(20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("Done!")