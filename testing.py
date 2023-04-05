import numpy as np 
import scipy
import matplotlib.pyplot as plt
import time

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

if __name__ == "__main__":
    filename = "theodora_focused.csv"
    data = np.loadtxt(filename, delimiter=",", dtype=str)
    
    columnsNames = data[0]
    # timestampts = data[:, 0]
    data = data[1:-1]
    data = data.astype(float)
    TP9 = data[1:-1, 1]
    AF7 = data[1:-1, 2]
    AF8 = data[1:-1, 3]
    TP10 = data[1:-1, 4] 
    s = TP9 + AF7 + AF8 + TP10

    plt.figure(filename)

    sampleRate = int(len(s)/60)
    timeVector = [i for i in range(len(s))]
    plt.subplot(311)
    plt.plot(timeVector, s)


    alpha = lowPassFilter(s, 12, sample_frequency=sampleRate)
    beta = bandPassFilter(s, 13, 30, sample_frequency=sampleRate)
    gamma = highPassFilter(s, 32, sample_frequency=sampleRate)



    windowCount = 60
    w_timeVector = [i for i in range(windowCount)]
    p_alpha = powerPerWindow(alpha, windowCount)
    p_beta = powerPerWindow(beta, windowCount)
    p_gamma = powerPerWindow(gamma, windowCount)

    plt.subplot(312)
    plt.title("power per window")
    plt.plot(w_timeVector, p_alpha, "b", label="alpha")
    plt.plot(w_timeVector, p_beta, "r", label="beta")
    plt.plot(w_timeVector, p_gamma, "g", label="gamma")
    plt.legend()

    plt.subplot(3,1,3)
    xf, s_fft  = get_fft(s, sampleRate)
    plt.plot(xf, s_fft)
    print(s_fft)
    plt.xlim([0, 40])

    plt.show()












    exit()


    # 14133 samples over 60 seconds  
    # 235 samples per second 
    # 2350 sample per 10 seconds window

    plt.subplot(3,1,1)
    sensorTimeVector = [i for i in range(len(TP9))]
    plt.title("Sensors Data")
    plt.plot(sensorTimeVector, TP9, label="TP9")
    plt.plot(sensorTimeVector, TP10, label="TP10")
    plt.plot(sensorTimeVector, AF7, label="AF7")
    plt.plot(sensorTimeVector, AF8, label="AF8")
    plt.legend()


    windowsCount = 1000
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
   
    alpha_mean = np.mean(alpha_all)
    beta_mean = np.mean(beta_all)
    gamma_mean = np.mean(gamma_all)

    print("alpha %f, beta %f, gamma %f"%(alpha_mean, beta_mean, gamma_mean))

    power_alpha_all = powerPerWindow(alpha_all, windowsCount)
    power_beta_all = powerPerWindow(beta_all, windowsCount)
    power_gamma_all = powerPerWindow(gamma_all, windowsCount)

    plt.subplot(3,1,2)
    xf, s_fft  = get_fft(s, 255)
    plt.plot(xf, s_fft)



    plt.subplot(3,1,3)
    plt.title("Power")
    plt.plot(timeVector, power_alpha_all, "b", label="power_alpha_all")
    plt.plot(timeVector, power_beta_all, "g", label="power_beta_all")
    plt.plot(timeVector, power_gamma_all, "r", label="power_gamma_all")
    plt.legend()
    plt.show()








