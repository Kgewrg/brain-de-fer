import mindwave, time, datetime,random
import numpy as np
import joblib


def main():
    print('Connecting to Mindwave...')
    headset = mindwave.Headset('COM10')

    print('Connected, waiting 10 seconds for data to start streaming')
    time.sleep(10)

    testtime=100000 #minutes

    future = time.time() + 60 * testtime
        
    while time.time() < future:    
        number = random.randint(30, 100)#bot player 
        print(headset.attention,"  poor ",headset.poor_signal)
        try:
            with open("C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\data.csv", "w") as f :
                f.write(str(headset.attention)+","+str(number))
        except (PermissionError):
            print("File was not opened: skiping")
        print("wrote to file:", headset.attention)
        time.sleep(1)

if __name__ == "__main__":
    main()
