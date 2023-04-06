import numpy as np 
import scipy
import matplotlib.pyplot as plt
import time




def bandPassFilter(signal, lowcut, highpass):
    sfreq = 2000.0 #Sampling freq

    nyq = 0.5 * sfreq
    low = lowcut / nyq
    high = highpass / nyq

    order = 2

    b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y

def highPassFilter(signal, hz):
    sfreq = 2000.0 #Sampling freq

    nyq = 0.5 * sfreq
    high = hz / nyq

    order = 2

    b, a = scipy.signal.butter(order, high, 'highpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y

def lowPassFilter(signal, hz):
    sfreq = 2000.0 #Sampling freq

    nyq = 0.5 * sfreq
    low = hz / nyq

    order = 2

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




if __name__ == "__main__":

    sampleRate = 2000
    duration = 2 # seconds
    tv = np.arange(0, duration, 1/sampleRate)

    w1 = 2.0 * np.pi * 10
    w2 = 2.0 * np.pi * 20
    w3 = 2.0 * np.pi * 40

    N = sampleRate * duration
    s = 10 * np.sin(tv*w1) +   np.sin(tv*w2) +  np.sin(tv*w3)


    alpha = lowPassFilter(s, 12)
    beta = bandPassFilter(s, 13, 30)
    gamma = highPassFilter(s, 32)

    n_windows = 10
    p_s = powerPerWindow(s, n_windows)
    p_alpha = powerPerWindow(alpha, n_windows)
    p_beta = powerPerWindow(beta, n_windows)
    p_gamma = powerPerWindow(gamma, n_windows)
    powerTV = np.arange(0, n_windows, 1)


    xf, s_fft  = get_fft(s, sampleRate)
    plt.subplot(311)
    plt.plot(s)
    plt.grid()
    plt.subplot(312)
    plt.plot(xf, np.abs(s_fft))
    plt.grid()

    plt.subplot(313)
    plt.plot(powerTV, p_s, label="original")
    plt.plot(powerTV, p_alpha, label="alpha")
    plt.plot(powerTV, p_beta, label="beta")
    plt.plot(powerTV, p_gamma, label="gamma")
    plt.legend()
    plt.grid()



    plt.show()





