import numpy as np 
import scipy
import matplotlib.pyplot as plt
import time

def bandPassFilter(signal, lowcut, highpass):
    sfreq = 256.0 #Sampling freq

    nyq = 0.5 * sfreq
    low = lowcut / nyq
    high = highpass / nyq

    order = 8

    b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y

def highPassFilter(signal, hz):
    sfreq = 256.0 #Sampling freq

    nyq = 0.5 * sfreq
    high = hz / nyq

    order = 8

    b, a = scipy.signal.butter(order, high, 'highpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y

def lowPassFilter(signal, hz):
    sfreq = 256.0 #Sampling freq

    nyq = 0.5 * sfreq
    low = hz / nyq

    order = 8

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

if __name__ == "__main__":
    fileName = "tsaros_unfocused.csv"
    data = np.loadtxt(fileName, delimiter=",", dtype=str)
    
    columnsNames = data[0]
    # timestampts = data[:, 0]
    data = data[1:-1]
    data = data.astype(float)
    TP9 = data[1:-1, 1]
    AF7 = data[1:-1, 2]
    AF8 = data[1:-1, 3]
    TP10 = data[1:-1, 4] 


    # 14133 samples over 60 seconds  
    # 235 samples per second 
    # 2350 sample per 10 seconds window

    plt.figure(fileName)
    plt.subplot(2,1,1)
    sensorTimeVector = [i for i in range(len(TP9))]
    plt.title("Sensors Data")
    plt.plot(sensorTimeVector, TP9, label="TP9")
    plt.plot(sensorTimeVector, TP10, label="TP10")
    plt.plot(sensorTimeVector, AF7, label="AF7")
    plt.plot(sensorTimeVector, AF8, label="AF8")
    plt.legend()

    windowsCount = 60
    timeVector = [i for i in range(windowsCount)]

    af7_alpha = lowPassFilter(AF7, 12)
    af7_beta = bandPassFilter(AF7, 13, 30)
    af7_gamma = highPassFilter(AF7, 32)

    af8_alpha = lowPassFilter(AF8, 12)
    af8_beta = bandPassFilter(AF8, 13, 30)
    af8_gamma = highPassFilter(AF8, 32)

    tp9_alpha = lowPassFilter(TP9, 12)
    tp9_beta = bandPassFilter(TP9, 13, 30)
    tp9_gamma = highPassFilter(TP9, 32)

    tp10_alpha = lowPassFilter(TP10, 12)
    tp10_beta = bandPassFilter(TP10, 13, 30)
    tp10_gamma = highPassFilter(TP10, 32)

    alpha_all = (af7_alpha + af8_alpha + tp9_alpha + tp10_alpha)  
    beta_all = (af7_beta + af8_beta + tp9_beta + tp10_beta) 
    gamma_all = (af7_gamma + af8_gamma + tp9_gamma + tp10_gamma) 


    SAMPLE_RATE = int(len(alpha_all)/60)
    DURATION = 60 # seconds
    N = SAMPLE_RATE * DURATION


    alpha_fft = scipy.fft.fft(alpha_all)
    beta_fft = scipy.fft.fft(beta_all)
    gamma_fft = scipy.fft.fft(gamma_all)

    xf = scipy.fft.fftfreq(N, 1 / SAMPLE_RATE)

    plt.subplot(2,1,2)
    plt.plot(xf, np.abs(alpha_fft[0:len(xf)]), label="alpha")
    plt.plot(xf, np.abs(beta_fft[0:len(xf)]), label="beta")
    plt.plot(xf, np.abs(gamma_fft[0:len(xf)]), label="gamma")
    plt.legend()

    



    alpha_mean = np.mean(alpha_all)
    beta_mean = np.mean(beta_all)
    gamma_mean = np.mean(gamma_all)

    print("alpha %f, beta %f, gamma %f"%(alpha_mean, beta_mean, gamma_mean))

    power_alpha_all = powerPerWindow(alpha_all, windowsCount)
    power_beta_all = powerPerWindow(beta_all, windowsCount)
    power_gamma_all = powerPerWindow(gamma_all, windowsCount)


 
    plt.show()







