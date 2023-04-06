from muselsl import *
import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft


def main():
    path=os.getcwd()+"\sfak_focused.csv"
    #record_muse(60,path)
    
    dataset = pd.read_csv(path)
    dataset=dataset.values# np array with dataset 9-40 hz
    dataset=np.delete(dataset,0,1)
    dataset=np.delete(dataset,-1,1)

    # fs=256  #sampling frequency
    
    # Alpha=lowpass_filter(dataset,13)#9-13
    # Beta=bandPassFilter(dataset,13,30)#13-30
    # Gamma=bandPassFilter(dataset,30,40)#30-40

    Alpha,Beta,Gamma=computeRythms(dataset)

    Alpha=removeOddValues(Alpha)
    Beta=removeOddValues(Beta)
    Gamma=removeOddValues(Gamma)

    spectrumΕnergy(Alpha)
    spectrumΕnergy(Beta)
    spectrumΕnergy(Gamma)

    plotSpecEnergy(Alpha,Beta,Gamma)

def computeRythms(dataset):

    TP9=dataset[:,0]
    AF7=dataset[:,1]
    AF8=dataset[:,2]
    TP10=dataset[:,3]

    TP9=bandPassFilter(TP9,9,40)
    AF7=bandPassFilter(AF7,9,40)
    AF8=bandPassFilter(AF8,9,40)
    TP10=bandPassFilter(TP10,9,40)

    Alpha1=lowpass_filter(TP9,13)
    Alpha2=lowpass_filter(AF7,13)
    Alpha3=lowpass_filter(AF8,13)
    Alpha4=lowpass_filter(TP10,13)

    Beta1=bandPassFilter(TP9,13,30)
    Beta2=bandPassFilter(AF7,13,30)
    Beta3=bandPassFilter(AF8,13,30)
    Beta4=bandPassFilter(TP10,13,30)

    Gamma1=bandPassFilter(TP9,30,40)#30-40
    Gamma2=bandPassFilter(AF7,30,40)#30-40
    Gamma3=bandPassFilter(AF8,30,40)#30-40
    Gamma4=bandPassFilter(TP10,30,40)#30-40

    Alpha=(Alpha1+Alpha2+Alpha3+Alpha4)/4
    Beta=(Beta1+Beta2+Beta3+Beta4)/4
    Gamma=(Gamma1+Gamma2+Gamma3+Gamma4)/4

    
    return Alpha,Beta,Gamma

#Function that cumputes the specturm energy
#1)Multiply each value of the fft output with it's conjugate
#2)Sum all the values after the multiplication
#3)Multiply the Sum with the quantum of time (1/number of samples)
def spectrumΕnergy(rythm):
    rythm=fft(rythm)
    length=len(rythm)
    sumconj=rythm*np.conj(rythm)
    specEn=sum([sumconj[i] for i in range(length)])
    specEn=specEn/length
    print("The energy is :" ,specEn)

def removeOddValues(rythm):
    length=len(rythm)
    rythm=fft(rythm)
    conjrythm=np.conj(rythm)
    rythm=rythm * conjrythm
    meanofrythm=np.mean(rythm)
    sum=0
    counter=0
    for i in range(len(rythm)):
        if(rythm[i] > meanofrythm):
            sum+=rythm[i]
            counter+=1
    mymean=sum/counter
    for i in range(length):
        if rythm[i] > 3*mymean:
            rythm[i]=mymean

    rythm=rythm/conjrythm
    rythm=scipy.fft.ifft(rythm)
    return rythm

def plotSpecEnergy(Alpha,Beta,Gamma):
    length=len(Alpha)
    fs=256
    Alpha=fft(Alpha)
    Beta=fft(Beta)
    Gamma=fft(Gamma)
    
    f = fs * np.arange(0, int(length/2)) / length
    Alpha=Alpha[0:int(length/2)]
    Beta=Beta[0:int(length/2)]
    Gamma=Gamma[0:int(length/2)]

    fig,ax= plt.subplots(2,2)

    ax[0,0].plot(f,(np.abs(Alpha)**2)/length)
    ax[0,0].grid()
    ax[0,0].legend(["Alpha"],loc="upper right")
    ax[0,0].set_xlabel('(Hz)',fontweight='bold'),
    ax[0,0].set_ylabel('Power energy spectrum (Joules)',fontweight='bold')
    ax[0,1].plot(f,(np.abs(Beta)**2)/length)
    ax[0,1].grid()
    ax[0,1].legend(["Beta"],loc="upper right")
    ax[0,1].set_xlabel('(Hz)',fontweight='bold'),
    ax[0,1].set_ylabel('(Joules)',fontweight='bold')
    ax[1,0].plot(f,(np.abs(Gamma)**2)/length)
    ax[1,0].grid()
    ax[1,0].legend(["Gamma"],loc="upper right")
    ax[1,0].set_xlabel('(Hz)',fontweight='bold'),
    ax[1,0].set_ylabel('(Joules)',fontweight='bold')
    plt.show()

def record_muse(time,path):#function that records with muse
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

    df=pd.DataFrame(y,columns=['TP9','AF7','AF8','TP10'])
    df.to_csv(filename,index=False)

def bandPassFilter(signal, lowcut, highpass):
    sfreq = 256.0 #Sampling freq

    nyq = 0.5 * sfreq
    low = lowcut / nyq
    high = highpass / nyq

    order = 4

    b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y

def lowpass_filter(signal,cutOff):
    fs=256
    order=4
    nyq = 0.5 * fs
    normalCutoff = cutOff / nyq
    b, a = scipy.signal.butter(order, normalCutoff, btype='low', analog = False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)
    return y

if __name__ == "__main__":
    main()
