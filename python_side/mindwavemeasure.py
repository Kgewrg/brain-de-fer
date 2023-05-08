import mindwave, time, datetime,random,pandas as pd

print('Connecting to Mindwave...')
headset = mindwave.Headset('COM3')

print('Connected, waiting 10 seconds for data to start streaming')
time.sleep(10)
#time for recording
testtime=1 #minutes

now = time.time()
future = now + 60 * testtime
    # text = str(headset.poor_signal) + "," + str(headset.raw_value) + "," + str(headset.attention) + "," + str(headset.meditation) 
    #f.write("poor_signal , raw,attention , meditation\n")
with open("C:/Users/Nikos/Desktop/brain-de-fair/python_side/mindwave_dataset/pal_focused.csv", "w") as f :

# attention , meditation, low-alpha , high alpha , low-beta, high-beta , low gamma, mid-gamma, raw_value, delta , theta
    while time.time() < future:
        # temp=" "
        # for i in range(len(headset.waves)):
        #     temp+=str(headset.waves[i])+","
        text=str(headset.attention)+","+str(headset.meditation)+","+str(headset.waves['low-alpha'])+","+str(headset.waves['high-alpha'])+","+str(headset.waves['low-beta'])+","+str(headset.waves['high-beta'])+","+str(headset.waves['low-gamma'])+","+str(headset.waves['mid-gamma'])+","+str(headset.raw_value)+","+str(headset.waves['delta'])+","+str(headset.waves['theta'])

        print(text)
        print("poor value  "+str(headset.poor_signal)+"  ----------------")
                
        f.write(text + "\n")
        time.sleep(1/100)