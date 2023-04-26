import numpy as np 
import scipy
import matplotlib.pyplot as plt
import time

from scipy.fft import fft


def bandPassFilter(signal, lowcut, highpass, sample_frequency=256.5, order = 8):
    sfreq = sample_frequency #Sampling freq

    nyq = 0.5 * sfreq
    low = lowcut / nyq
    high = highpass / nyq



    b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y

def highPassFilter(signal, hz, sample_frequency=256.5, order = 8):
    sfreq = sample_frequency #Sampling freq

    nyq = 0.5 * sfreq
    high = hz / nyq


    b, a = scipy.signal.butter(order, high, 'highpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y

def lowPassFilter(signal, hz, sample_frequency=256.5, order = 8):
    sfreq = sample_frequency #Sampling freq

    nyq = 0.5 * sfreq
    low = hz / nyq


    b, a = scipy.signal.butter(order, low, 'lowpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y


def powerPerWindow(signal, windowCount):
    signalSize = len(signal)
    samplesPerWindow = int(signalSize/windowCount)
    results = [0 for i in range(windowCount)]
    for i in range(windowCount):
        start = i * samplesPerWindow
        end = (i+1) * samplesPerWindow
        s = 0 
        for j in signal[start:end]:
            s += j*j
        wPower = s/samplesPerWindow
        results[i] = wPower
    return(results)

def get_fft(traces, sampling_frequency):
    # Return the power spectrum of the positive fft
    N = len(traces)
    yf = np.fft.fft(traces)
    # Get only positive freqs
    xf = np.fft.fftfreq(N, 1/sampling_frequency)[:N//2]
    nyf = 2.0/N * np.abs(yf)[:N//2]
    return xf, nyf



def removeOddValues(rythm):
    mymean=findMeanOfChannel(rythm)
    rythm=fft(rythm)
    conjrythm=np.conj(rythm)
    rythm=rythm * conjrythm
    for i in range(len(rythm)):
        if rythm[i] > 13*mymean:
            rythm[i]=mymean
    rythm=rythm/conjrythm
    rythm=scipy.fft.ifft(rythm)
    return rythm


def findMeanOfChannel(rythm):
    rythm=fft(rythm)
    rythm=np.abs(rythm)**2
    meanofrythm=np.mean(rythm)
    sum=0
    counter=0
    for i in range(len(rythm)):
        if(rythm[i] > 10000):
            sum+=rythm[i]
            counter+=1
    mymean=sum/counter
    return mymean



if __name__ == "__main__":
    
    
    focused_fn = "theodora_focused.csv"
    unfocused_fn = "tsaros_unfocused.csv"
    # focused_fn = "my_focused_open.csv"
    # unfocused_fn = "my_unfocused_closed.csv"
    
    unfocused = np.loadtxt("muse_dataset/"+unfocused_fn, delimiter=",", dtype=str)
    focused = np.loadtxt("muse_dataset/"+focused_fn, delimiter=",", dtype=str)

    unfocused = unfocused[1:]
    unfocused = unfocused.astype(float)
    
    focused = focused[1:]
    focused = focused.astype(float)
    
    
    
    start_focused = focused[:, 1] + focused[:, 2] + focused[:, 3] + focused[:, 4]
    start_unfocused = unfocused[:, 1] + unfocused[:, 2] + unfocused[:, 3] + unfocused[:, 4]
    
    
    timeVector = [i for i in range(len(focused))]
    sampleRate = int(len(focused)/60)
    
    
    focused = start_focused.copy()
    unfocused = start_unfocused.copy()
    
    # # normalize the 2 signals
    # focused = focused / np.linalg.norm(focused)
    # unfocused = unfocused / np.linalg.norm(unfocused)
    
   
    
    f_mean = np.average(focused)
    un_mean  = np.average(unfocused)
    
    focused = focused - f_mean
    unfocused = unfocused - un_mean
    
   

    focused = focused - lowPassFilter(focused, 4, sampleRate)
    unfocused = unfocused - lowPassFilter(unfocused, 4, sampleRate)

    f_alpha = lowPassFilter(focused, 12, sampleRate)
    f_beta = bandPassFilter(focused, 13, 30, sampleRate)
    f_gamma = bandPassFilter(focused, 32, 40, sampleRate)
    
    
    un_alpha = lowPassFilter(unfocused, 12, sampleRate)
    un_beta = bandPassFilter(unfocused, 13, 30, sampleRate)
    un_gamma = bandPassFilter(unfocused, 32, 40, sampleRate)
    
    
    windowCount = 20
    f_b_power = powerPerWindow(f_beta, windowCount)
    f_g_power = powerPerWindow(f_gamma, windowCount)
    
    un_b_power = powerPerWindow(un_beta, windowCount)
    un_g_power = powerPerWindow(un_gamma, windowCount)
    
    # print("focused   | g=%.2f, b=%.2f"%(np.average(f_g_power), np.average(f_b_power)))
    # print("unfocused | g=%.2f, b=%.2f"%(np.average(un_g_power), np.average(un_b_power)))
    
    # plt.subplot(121)
    # plt.title("gamma")
    # plt.plot(f_g_power, "r", label="focused")
    # plt.plot(un_g_power, "b", label="unfocused")
    # plt.legend()
    
    # plt.subplot(122)
    # plt.title("beta")
    # plt.plot(f_b_power, "r", label="focused")
    # plt.plot(un_b_power, "b", label="unfocused")
    # plt.legend()
    # plt.show()
    
    a = 0.3
    b = 0.7
    
    f_comb = np.add(np.dot(a, f_b_power), np.dot(b, f_g_power))
    un_comb = np.add(np.dot(a, un_b_power), np.dot(b, un_g_power))
    
    print("a=%.1f b=%.1f"%(a, b))
    print("focused   : %.2f"%(np.average(f_comb)))
    print("unfocused : %.2f"%(np.average(un_comb)))
    
    plt.plot(f_comb, "r", label="focused")
    plt.plot(un_comb, "b", label="unfocused")
    plt.legend()
    plt.show()
   