import mindwave, time, datetime,random
import numpy as np
import joblib


filePath2 ="C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\egw2_focused.csv"
#filePath = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\data.csv"

def main():
    # Αρχικοποίηση του αρχείου σε αρχικές τιμές
    open(filePath2, "w").write("0,0")

    print('Connecting to Mindwave...')
    headset = mindwave.Headset('COM3')

    print('Connected, waiting 6 seconds for data to start streaming')
    time.sleep(6)

    testtime=2 #minutes

    Model=joblib.load("RandomForestModel.pkl")
    now = time.time()
    future = now + 60 * testtime
    result=[]
    with open(filePath2,"w") as f:     
        while time.time() < future: 
            measurements=[]
            temp=time.time()
            while( time.time() < temp + 1 ):
                
                temparray = np.array([(headset.attention),(headset.meditation),(headset.raw_value)])
                #temparray = np.array([(headset.attention),(headset.meditation),(headset.waves['low-alpha']),(headset.waves['high-alpha']),(headset.waves['low-beta']),(headset.waves['high-beta']),(headset.waves['low-gamma']),(headset.waves['mid-gamma']),(headset.raw_value),(headset.waves['delta']),(headset.waves['theta'])])
                measurements.append(temparray)
                time.sleep(1/128)
            player1=calculate_percentage(measurements,Model)
            print(headset.poor_signal)
            f.write(str(player1) + "," + str(headset.attention) +"\n")
            print("wrote to file:", player1,"   Mindwave: ",headset.attention)

def calculate_percentage(measurements,Model):
    result=Model.predict(measurements)
    return np.sum(result)*100/len(result)

if __name__ == "__main__":
    main()
