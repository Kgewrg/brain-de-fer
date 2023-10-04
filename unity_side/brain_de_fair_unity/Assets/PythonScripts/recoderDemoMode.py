import mindwave, time, random

filePath = "data.csv"

def main():
    # Αρχικοποίηση του αρχείου σε αρχικές τιμές
    open(filePath, "w").write("0,0,0,0,0,0")

    # print('Connecting to Mindwave...')
    # headset1 = mindwave.Headset('COM3')
    # print('Connected, waiting 5 seconds for data to start streaming')
    # time.sleep(9)
    
    testtime=100000 #minutes

    future = time.time() + 60 * testtime


    while time.time() < future:    
        # print("1st poor  ",headset1.poor_signal)
        try:
            with open(filePath, "w") as f :
                testing = random.randint(40, 80)
                f.write(str(testing)+","+"0"+",1,1,"+'0'+","+"300") 
                # θα πρέπει να γίνει κάτι πιο σωστό για την δευτερη συσκευή
            print("wrote to file:",testing)
            time.sleep(0.9)
     
        except PermissionError as PE:
            print("File was not opened: skiping")


if __name__ == "__main__":
    main()


