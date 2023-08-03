from muselsl import *
import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft


def main():
    path1=os.path.dirname(__file__)+"\muse_dataset\\subject3_focused.csv"
    path2=os.path.dirname(__file__)+"\muse_dataset\\subject3_relaxed.csv"
    path3=os.path.dirname(__file__)+"\muse_dataset\\subject4_focused.csv"
    path4=os.path.dirname(__file__)+"\muse_dataset\\subject4_relaxed.csv"
    pathArray=[path1,path2]
    for i in pathArray:
        name= ""
        for j in i[::-1]:
            if j=="\\":
                break
            name=name + j
        name=name[::-1]
        print("--------------------")
        print("Dataset : ",name)
        print("--------------------")
        dataset = pd.read_csv(i)
        dataset=dataset.values# np array with dataset 9-40 hz
        dataset=np.delete(dataset,0,1)
        

        Alpha,Beta,Gamma=computeRythms(dataset)

        Alpha=removeOddValues(Alpha,8,12)
        Beta=removeOddValues(Beta,13,30)
        Gamma=removeOddValues(Gamma,31,50)

        # a=int(np.sqrt(findMeanOfChannel(Alpha)))
        # b=int(np.sqrt(findMeanOfChannel(Beta)))
        # g=int(np.sqrt(findMeanOfChannel(Gamma)))
        # ena=a/b
        # duo=a/g
        #print("-----------------")
        # print("%.3f" % ena)
        # print("%.3f" % duo)

        # spectrumΕnergy(Alpha)
        # spectrumΕnergy(Beta)
        # spectrumΕnergy(Gamma)

        plotSpecEnergy(Alpha,Beta,Gamma,name)
        
def computeRythms(dataset):

    TP9=dataset[:,0]
    AF7=dataset[:,1]
    AF8=dataset[:,2]
    TP10=dataset[:,3]

    TP9=bandPassFilter(TP9,8,50)
    AF7=bandPassFilter(AF7,8,50)
    AF8=bandPassFilter(AF8,8,50)
    TP10=bandPassFilter(TP10,8,50)

    Alpha1=lowpass_filter(TP9,12)
    Alpha2=lowpass_filter(AF7,12)
    Alpha3=lowpass_filter(AF8,12)
    Alpha4=lowpass_filter(TP10,12)

    AlphaArray=[Alpha1,Alpha2,Alpha3,Alpha4]
    arrayofmean=[]
    # for i in range(len(AlphaArray[:])):
    #     arrayofmean.append(int(np.sqrt(findMeanOfChannel(AlphaArray[i]))))
    # print("Alpha ",arrayofmean)
        
    
    Beta1=bandPassFilter(TP9,13,30)
    Beta2=bandPassFilter(AF7,13,30)
    Beta3=bandPassFilter(AF8,13,30)
    Beta4=bandPassFilter(TP10,13,30)
    BetaArray=[Beta1,Beta2,Beta3,Beta4]
    arrayofmean=[]
    # for i in range(len(AlphaArray[:])):
    #     arrayofmean.append(int(np.sqrt(findMeanOfChannel(BetaArray[i]))))
    # print("Beta ",arrayofmean)

    
    Gamma1=bandPassFilter(TP9,31,50)#30-40
    Gamma2=bandPassFilter(AF7,31,50)#30-40
    Gamma3=bandPassFilter(AF8,31,50)#30-40
    Gamma4=bandPassFilter(TP10,31,50)#30-40
    GammaArray=[Gamma1,Gamma2,Gamma3,Gamma4]
    arrayofmean=[]
    # for i in range(len(AlphaArray[:])):
    #     arrayofmean.append(int(np.sqrt(findMeanOfChannel(GammaArray[i]))))
    # print("Gamma ",arrayofmean)

    

    Alpha=(Alpha1+Alpha2+Alpha3+Alpha4)
    Beta=(Beta1+Beta2+Beta3+Beta4)
    Gamma=(Gamma1+Gamma2+Gamma3+Gamma4)
    

    
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

def removeOddValues(rythm,low,high):
    #---compute the fft of rythm and remove the complex numbers ---#
    length=len(rythm)
    rythm=fft(rythm)
    conjrythm=np.conj(rythm)
    rythm=rythm * conjrythm
    #--- find the mean of the given frequency range ---#
    freqs = 256 * np.arange(0, int(length/2)) / length
    freq_range = np.where((freqs >= low) & (freqs <= high))
    mymean = np.mean(rythm[freq_range])
    #--- normalize any value bigger than 8 time the mean of rythm ---#
    for i in range(length):
        if rythm[i] > 8*mymean:
            rythm[i]=mymean
    rythm=rythm/conjrythm
    rythm=scipy.fft.ifft(rythm)
    return rythm

def plotSpecEnergy(Alpha,Beta,Gamma,name):
    length=len(Alpha)
    fs=256
    T=fs*length
    Alpha=fft(Alpha)
    Beta=fft(Beta)
    Gamma=fft(Gamma)
    
    f = fs * np.arange(0, int(length/2)) / length
    Alpha=Alpha[0:int(length/2)]
    Beta=Beta[0:int(length/2)]
    Gamma=Gamma[0:int(length/2)]

    fig,ax= plt.subplots(2,2)
    fig.suptitle(name)
    ax[0,0].plot(f,(np.abs(Alpha)**2)/T)
    ax[0,0].grid()
    ax[0,0].legend(["Alpha"],loc="upper right")
    ax[0,0].set_xlabel('(Hz)',fontweight='bold'),
    ax[0,0].set_ylabel('Power energy spectrum (Joules)',fontweight='bold')
    ax[0,1].plot(f,(np.abs(Beta)**2)/T)
    ax[0,1].grid()
    ax[0,1].legend(["Beta"],loc="upper right")
    ax[0,1].set_xlabel('(Hz)',fontweight='bold'),
    ax[0,1].set_ylabel('(Joules)',fontweight='bold')
    ax[1,0].plot(f,(np.abs(Gamma)**2)/T)
    ax[1,0].grid()
    ax[1,0].legend(["Gamma"],loc="upper right")
    ax[1,0].set_xlabel('(Hz)',fontweight='bold'),
    ax[1,0].set_ylabel('(Joules)',fontweight='bold')
    plt.show()

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
