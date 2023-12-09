import mindwave, time, os



def main():
    
    # Find the current dir and add the data.csv file
    execPath = os.path.dirname(__file__)  
    dataFilePath = os.path.join(os.path.dirname(execPath), "brain_de_fair_unity_Data", "data.csv")
 
    print("Path of data file:", dataFilePath)

    # Αρχικοποίηση του αρχείου σε αρχικές τιμές
    open(dataFilePath, "w").write("0,0,0,0,0,0")

    print('Connecting to Mindwave...')
    headset1 = mindwave.Headset('COM4')
    headset2 = mindwave.Headset("COM6")
    print('Connected, waiting 3 seconds for data to start streaming')
    time.sleep(3)
       

    testtime=100000 #minutes

    future = time.time() + 60 * testtime


    while time.time() < future:    
        print("1st poor  ",headset1.poor_signal," 2nd poor   ",headset2.poor_signal)
        try:
            with open(dataFilePath, "w") as f :
                f.write(str(headset1.attention)+","+str(headset2.attention)+",1,1,"+str(headset1.poor_signal)+","+str(headset2.poor_signal)) 
            print("wrote to file:", headset1.attention," and ",headset2.attention)
            time.sleep(0.9)
     
        except PermissionError as PE:
            print("File was not opened: skiping")


if __name__ == "__main__":
    main()



