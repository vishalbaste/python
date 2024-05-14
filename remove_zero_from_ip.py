def removeZeroFromIp(ip):
    ipArray = ip.split('.')
    removedArray = []

    for i in ipArray:
        removedArray.append(str(int(i)))

    outputIp = '.'.join(removedArray)

    print(f"Input : {ip} \n Output : {outputIp}")
        

removeZeroFromIp("192.01.010.001")