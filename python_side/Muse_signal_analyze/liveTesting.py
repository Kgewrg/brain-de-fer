import pylsl
import numpy as np
import testing

if __name__ == '__main__':
    streams = pylsl.resolve_byprop("type", "EEG")
    inlet = pylsl.StreamInlet(streams[0], max_chunklen=12)
    info = inlet.info()
    
    sampleFrequency = info.nominal_srate()
    windowCount = 20
    a = b = 1
    
    
    while True:

        data, timeStamp = inlet.pull_chunk(timeout=1, max_samples=int(sampleFrequency))
        data = np.array(data)
        data = data.astype(float)
        
        signal = data[:, 1] + data[:, 2] + data[:, 3] + data[:, 4]
        mean = np.average(data)
        signal = signal - mean
        
        signal = signal - testing.lowPassFilter(signal, 4, sampleFrequency)
        
        s_beta = testing.bandPassFilter(signal, 13, 30, sampleFrequency)
        s_gamma = testing.highPassFilter(signal, 32, sampleFrequency)

        s_b_power = testing.powerPerWindow(s_beta, 1)
        s_g_power = testing.powerPerWindow(s_gamma, 1)
        
        s_comp = np.add(np.dot(a, s_b_power), np.dot(b, s_g_power))
        print("%.2f"%(np.average(s_comp)))
        
        
        
        
       
        
