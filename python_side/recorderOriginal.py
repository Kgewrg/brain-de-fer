import mindwave, time, datetime,random
import numpy as np
import sys
import signal

# filePath = "C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\data.csv"
filePath = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\data.csv"
def main():
    open(filePath, "w").write("0,0,0")

    print('Connecting to Mindwave...')
    headset = mindwave.Headset('COM3')

    print('Connected, waiting 10 seconds for data to start streaming')
    time.sleep(5)
       

    testtime=100000 #minutes

    future = time.time() + 60 * testtime

    
    while time.time() < future:    
        # number = random.randint(30, 100)#bot player 
        number = 0 
        print(headset.attention,"  poor ",headset.poor_signal)
        try:
            with open(filePath, "w") as f :
                f.write(str(headset.attention)+","+str(number)+",1")
            print("wrote to file:", headset.attention)
            time.sleep(1)
     
        except PermissionError as PE:
            print("File was not opened: skiping")


if __name__ == "__main__":
    main()



