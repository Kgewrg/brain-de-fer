import random
import time
import os


fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "\\" + "value.txt")
print(fileName)
print()

while True:
    try:
        number = random.randint(0, 180)
        try:
            with open(fileName, "w") as f:
                f.write(str(number))
        except (PermissionError):
            print("File was opened: skiping")
        print("wrote to file:", number)
        time.sleep(1)


    except KeyboardInterrupt:
        if f:
            f.close()
        break


