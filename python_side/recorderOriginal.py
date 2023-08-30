import mindwave, time, datetime,random
import numpy as np
import joblib


def main():
    print('Connecting to Mindwave...')
    headset = mindwave.Headset('COM3')

    print('Connected, waiting 10 seconds for data to start streaming')
    time.sleep(10)

    testtime=100000 #minutes

    future = time.time() + 60 * testtime

    # filePath = "C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\data.csv"
    filePath = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\data.csv"
        
    while time.time() < future:    
        # number = random.randint(30, 100)#bot player 
        number = 0 
        print(headset.attention,"  poor ",headset.poor_signal)
        try:
            with open(filePath, "w") as f :
                f.write(str(headset.attention)+","+str(number))
        except (PermissionError):
            print("File was not opened: skiping")
        print("wrote to file:", headset.attention)
        time.sleep(1)

if __name__ == "__main__":
    main()
