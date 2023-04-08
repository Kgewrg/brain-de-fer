import mindwave, time, datetime

print('Connecting to Mindwave...')
headset = mindwave.Headset('COM9')

print('Connected, waiting 10 seconds for data to start streaming')
time.sleep(10)
#time for recording
testtime=3 #minutes

now = time.time()
future = now + 60 * testtime
with open("data.csv", "w+") as f :

    # writer.writerow(['Timestamp','Raw','Attention','Meditation','delta','theta','low-alpha','high-alpha','low-beta','high-beta','low-gamma','mid-gamma'])
    f.write("poor_signal , raw,attention , meditation\n")
    while time.time() < future:

        text= str(headset.poor_signal) + " , " + str(headset.raw_value)
        # text = str(headset.poor_signal) + "," + str(headset.raw_value) + "," + str(headset.attention) + "," + str(headset.meditation) 
        print(text)
        f.write(text + "\n")

        # print ("Raw value: %s, Attention: %s, Meditation: %s" % (headset.raw_value, headset.attention, headset.meditation))
        # values = list(headset.waves.values())

        # writer.writerow(values)
        time.sleep(1/10)
