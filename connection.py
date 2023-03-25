from muselsl import *
import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft




def main():
    path=os.getcwd()+"/Focused.csv"
    #record_muse(60,path)
    
    dataset = pd.read_csv(path)
    dataset=dataset.values# np array with dataset 9-40 hz
    TP9=dataset[:,0]
    AF7=dataset[:,1]
    AF8=dataset[:,2]
    TP10=dataset[:,3]

    
    
    fs=256  #sampling frequency

    Alpha=lowpass_filter(dataset,13)#9-13
    Beta=bandPassFilter(dataset,13,30)#13-30
    Gamma=bandPassFilter(dataset,30,40)#30-40
    plot(dataset)
    

def lowpass_filter(signal,cutOff):
    fs=256
    order=8
    nyq = 0.5 * fs
    normalCutoff = cutOff / nyq
    b, a = scipy.signal.butter(order, normalCutoff, btype='low', analog = False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)
    return y

def plot(dataset):#plots each sensor reading in the frequency dimension
    
    fs=256
    TP9=dataset[:,0]
    AF7=dataset[:,1]
    AF8=dataset[:,2]
    TP10=dataset[:,3]

    TP9=TP9-np.mean(TP9)
    AF7=AF7-np.mean(AF7)
    AF8=AF8-np.mean(AF8)
    TP10=TP10-np.mean(TP10)


    length= len(TP9)

    TP9=fft(TP9)
    TP10=fft(TP10)
    AF7=fft(AF7)
    AF8=fft(AF8)
    f = fs * np.arange(0, length/2) / length
   
    TP9= TP9[0:int(length/2)+1]
    TP10= TP10[0:int(length/2)+1]
    AF8= AF8[0:int(length/2)+1]
    AF7= AF7[0:int(length/2)+1]
    
    Null,ax= plt.subplots(2,2)
    
    ax[0,0].plot(f,abs(TP9),label="TP9")
    ax[0,0].grid()
    ax[0,0].legend(loc="upper right")
    ax[0,1].plot(f,abs(TP10),label="TP10")
    ax[0,1].grid()
    ax[0,1].legend(loc="upper right")
    ax[1,0].plot(f,abs(AF8),label="AF8")
    ax[1,0].grid()
    ax[1,0].legend(loc="upper right")
    ax[1,1].plot(f,abs(AF7),label="AF7")
    ax[1,1].grid()
    ax[1,1].legend(loc="upper right")
    plt.show()

def record_muse(time,path):#function that records with muse applies 9-40hz bandpass filter and saves the file to the given path
    #clean the csv file
    filename = path
    f = open(filename, "w+")
    f.close()

    #record EEG signal from muse
    record(time,path)

    dataset = pd.read_csv(path)
    dataset=dataset.values
    dataset=np.delete(dataset,0,1)

    f = open(path, "w+")
    f.close()

    y=bandPassFilter(dataset,9,40)

    df=pd.DataFrame(y,columns=['TP9','AF7','AF8','TP10'])
    df.to_csv(filename,index=False)


def bandPassFilter(signal, lowcut, highpass):
    sfreq = 256.0 #Sampling freq

    nyq = 0.5 * sfreq
    low = lowcut / nyq
    high = highpass / nyq

    order = 8

    b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y


if __name__ == "__main__":
    main()
