import time
import random
import os


def main():
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


if __name__ == "__main__":
    main()



