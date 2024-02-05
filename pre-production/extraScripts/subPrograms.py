import time
import extraScripts.mindwave as mindwave
import os
import random



# This class is defined because there were problems
# with imports on this and other files that were using
# these functions

class extraScripts:
    def __init__(self) -> None:
        pass

    def DEMO():
        # Find the current dir and add the data.csv file
        execPath = os.path.dirname(__file__)  
        dataFilePath = os.path.join(os.path.dirname(execPath), "brain_de_fair_unity_Data", "data.csv")

        print("Path of data file:", dataFilePath)

        # Αρχικοποίηση του αρχείου σε αρχικές τιμές
        open(dataFilePath, "w").write("0,0,0,0,0,0")

        while True:    
            leftValue = random.randint(0, 100)
            rightValue = random.randint(0, 100)
            try:
                with open(dataFilePath, "w") as f :
                    f.write(str(leftValue)+","+str(rightValue)+",1,1,"+str(0)+","+str(0))  # str(0) is for poor
                    print("Wrote to file: (Left player:)", leftValue, "(Right player:)", rightValue)
                time.sleep(0.9)
        
            except PermissionError as PE:
                print("File was not opened: skiping")


    def PVE():
         # Find the current dir and add the data.csv file
        execPath = os.path.dirname(__file__)  
        dataFilePath = os.path.join(os.path.dirname(execPath), "brain_de_fair_unity_Data", "data.csv")

        print("Path of data file:", dataFilePath)

        # Αρχικοποίηση του αρχείου σε αρχικές τιμές
        open(dataFilePath, "w").write("0,0,0,0,0,0")

        print('Connecting to Mindwave...')
        headset1 = mindwave.Headset('COM7')
        print('Connected, waiting 3 seconds for data to start streaming')
        time.sleep(3)
        

        testtime=100000 #minutes

        future = time.time() + 60 * testtime


        while time.time() < future:    
            print("1st poor  ",headset1.poor_signal)
            try:
                with open(dataFilePath, "w") as f :
                    f.write(str(headset1.attention)+","+"0"+",1,1,"+str(headset1.poor_signal)+","+"300") 
                    # θα πρέπει να γίνει κάτι πιο σωστό για την δευτερη συσκευή
                print("wrote to file:", headset1.attention)
                time.sleep(0.9)
        
            except PermissionError as PE:
                print("File was not opened: skiping")


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
    print("No instrunction are given, passing")
    pass
    




