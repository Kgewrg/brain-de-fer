import random
import time
import os


#fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "\\" + "value.txt")
fileName="C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\data.csv"

while True:
    try:
        number2=random.randint(1, 100)
        number = random.randint(1, 100)
        values=str(number)+","+str(number2)
        try:
            with open(fileName, "w") as f:
                f.write(values)
        except (PermissionError):
            print("File was opened: skiping")
        print("wrote to file:", values)
        time.sleep(1)


    except KeyboardInterrupt:
        if f:
            f.close()
        break


