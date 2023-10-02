import mindwave, time

filePath = "C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\data.csv"
#filePath = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\data.csv"
def main():
    # Αρχικοποίηση του αρχείου σε αρχικές τιμές
    open(filePath, "w").write("0,0,0,0,0,0")

    print('Connecting to Mindwave...')
    headset1 = mindwave.Headset('COM3')
    print('Connected, waiting 5 seconds for data to start streaming')
    time.sleep(9)
       

    testtime=100000 #minutes

    future = time.time() + 60 * testtime


    while time.time() < future:    
        print("1st poor  ",headset1.poor_signal)
        try:
            with open(filePath, "w") as f :
                f.write(str(headset1.attention)+","+"0"+",1,1,"+str(headset1.poor_signal)+","+"300") 
                # θα πρέπει να γίνει κάτι πιο σωστό για την δευτερη συσκευή
            print("wrote to file:", headset1.attention)
            time.sleep(0.9)
     
        except PermissionError as PE:
            print("File was not opened: skiping")


if __name__ == "__main__":
    main()


