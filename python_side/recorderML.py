import mindwave, time, datetime,random
import numpy as np
import joblib


filePath = "C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\data.csv"
#filePath = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\data.csv"

def main():
    # Αρχικοποίηση του αρχείου σε αρχικές τιμές
    open(filePath, "w").write("0,0,0,0")

    print('Connecting to Mindwave...')
    headset = mindwave.Headset('COM3')

    print('Connected, waiting 5 seconds for data to start streaming')
    time.sleep(5)

    testtime=100000 #minutes

    Model=joblib.load("RandomForestModel.pkl")
    now = time.time()
    future = now + 60 * testtime
        
    while time.time() < future:
        measurements=[]
        temp=time.time()
        while( time.time() < temp + 1 ):
            temparray = np.array([(headset.attention),(headset.meditation),(headset.raw_value)])
            #temparray = np.array([(headset.attention),(headset.meditation),(headset.waves['low-alpha']),(headset.waves['high-alpha']),(headset.waves['low-beta']),(headset.waves['high-beta']),(headset.waves['low-gamma']),(headset.waves['mid-gamma']),(headset.raw_value),(headset.waves['delta']),(headset.waves['theta'])])
            measurements.append(temparray)
            time.sleep(1/128)
        player1=calculate_percentage(measurements,Model) 
        print(player1,"  poor ",headset.poor_signal)
        while 0==0:#sunglasses cool bruh?
            try:
                with open(filePath, "w") as f :
                    f.write(str(player1)+",0,1,1,"+str(headset.poor_signal)+",300")
                    break
            except (PermissionError):
                print("File was not opened: skiping")
        print("wrote to file:", player1)

def calculate_percentage(measurements,Model):
    result=Model.predict(measurements)
    return np.sum(result)*100/len(result)

if __name__ == "__main__":
    main()
