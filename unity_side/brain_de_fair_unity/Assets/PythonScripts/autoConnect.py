import serial.tools.list_ports
import mindwave
import time
import threading
from collections import deque


def checkPoor():
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
            print (poorStatus, "increasing counter", badCounter)

            if (badCounter == numOfTries):
                print("Connection failed")
                connStatus = -1 
                break


        elif  (poorStatus == 200):
            print ("-- Connected")
            connStatus = 0 # linux style return code
            break 
        
        else:
            print("establishing connection")
            badCounter = 0
        
        time.sleep(1)

    return connStatus
        
def makeQueue(portList):
    tmp = deque()
    for i in portList:
        tmp.append(i)

    return tmp.copy()



# Get a list of all available ports
available_ports = serial.tools.list_ports.comports()

totalPorts = len(available_ports)
if (totalPorts == 0):
    print("No available COMM Ports, exiting")
    exit(-1)

print("Total number of ports:", totalPorts)
print("Port names")
# Get all port names in a list
strPortList = []
portQueue = deque()
for port in available_ports:
    print(port)
    strPortList.append(port.name)
    portQueue = makeQueue(strPortList)

deviceCount = 1
print("Searching for", deviceCount, "device(s)")
connectedDevices = [[0, 0, 0] for i in range(deviceCount)]
connectedDevicesCount = 0




portIndex = 0
while True:

    

    try:
        del headset
    except NameError:
        pass


    # Αν δοκίμασε όλες τις πόρτες 
    if (len(portQueue) == 0):
        # θα ξανα αρχήσει να ψάνχει απο την αρχή
        print("Exhausted all available ports, re-trying from the start")
        portQueue = makeQueue(strPortList)
        print() # empty line
        time.sleep(2)
        continue

    # Αν βρήκε όλες τις συσκευές
    if (connectedDevicesCount == deviceCount):
        print("Found all devices")
        for device in connectedDevices:
            print(device)
        exit(1)
    
    currentPort = portQueue.popleft()

    
    print()
    print ("Trying port:", currentPort)
    try:    
        headset = mindwave.Headset(currentPort)

    except Exception as e:
        # Αν μπει εδω, δεν θα ελεγξει poor
        print ("got exception: ", e)
        print ("Continiuing to next port")
        continue 

    # Αν έχει φτάσει εδώ, σημαίνει οτι δεν έφαγε error
    # Τωρα θέλει να ελεγξει για poor
    connStatus = checkPoor()

    if (connStatus == -1):
        print("bad port, continiuing to the next one")
        headset.stop()
        continue

    elif (connStatus == 0):
        connectedDevicesCount += 1
        print("Found the correct port: ", currentPort, "for device:", connectedDevicesCount)
        connectedDevices[connectedDevicesCount - 1] = [1, currentPort, headset.headset_id]
        strPortList.pop(strPortList.index(currentPort))
        continue
    


    

    time.sleep(1)





        




