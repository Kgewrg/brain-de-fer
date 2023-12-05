import time
import random
import os


def main():
    # Find the current dir and add the data.csv file
    filePath = os.path.dirname(__file__) + "\\"+ "data.csv" 
    print("Path of data file:", filePath)

    # Αρχικοποίηση του αρχείου σε αρχικές τιμές
    open(filePath, "w").write("0,0,0,0,0,0")

    while True:    
        leftValue = random.randint(0, 100)
        rightValue = random.randint(0, 100)
        try:
            with open(filePath, "w") as f :
                f.write(str(leftValue)+","+str(rightValue)+",1,1,"+str(0)+","+str(0))  # str(0) is for poor
                print("Wrote to file: (Left player:)", leftValue, "(Right player:)", rightValue)
            time.sleep(0.9)
     
        except PermissionError as PE:
            print("File was not opened: skiping")


if __name__ == "__main__":
    main()



