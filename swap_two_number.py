try:
    x = 10
    y = 20

    #Way one
    '''
        x = x + y
        y = x - y
        x = x - y
    '''

    #way two
    x,y = y,x
    
    print(f" After swap x is {x} and Y is {y}")
except:
    print("Opps! somthing went wrong")