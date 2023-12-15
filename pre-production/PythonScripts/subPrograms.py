import time
import mindwave



def checkPoor(headset):
    """
    Checks the poor value a couple of times 
    
    Returns:
        int: -1 = failed, 1 = connected
    """
    "Fetches a couple of poor values to see if the devices connected successfully"
    numOfTries = 8
    
    badCounter = 0

    connStatus = 0

    while True:
        poorStatus = headset.poor_signal
        
        if (poorStatus == 255):
            badCounter += 1
            print ("poor value:", poorStatus, "retrying", badCounter)

            if (badCounter == numOfTries):
                print("Connection failed")
                connStatus = -1 
                break


        elif  (poorStatus == 200):
            print ("-- Connected")
            connStatus = 1
            break 
        
        else:
            print("establishing connection")
            badCounter = 0
        
        time.sleep(1)

    return connStatus
        

def checkPort(port: str):
    connStatus = 0 # linux style return code (0 is good)

    try:
        print ("Trying to connect to port", port)
        headset = mindwave.Headset(port)

    except Exception as e:
        print("Error at connecting, probably non-existant port")
        print("---")
        print(e)
        return -1
    
    print("Connected to port, testing if the port is correct")
    time.sleep(3)
    result = checkPoor(headset)

    if (result == -1):
        print("Wrong port")
        connStatus = -1
    
    else:
        print("Correct port found")



    headset.stop()
    del headset
    return connStatus # linux style return code

    




if (__name__ == "__main__"):

    checkPort("COM4")




