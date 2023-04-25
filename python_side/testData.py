import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


# focused
def main():
    pathfoc=os.getcwd()+"\python_side\mindwave_dataset/pal_focused.csv"
    pathnotfoc=os.getcwd()+"\python_side\mindwave_dataset/pal_unfocused.csv"
    poor,raw,foc,med=getData(pathfoc)
    poor,raw,notfoc,notmed=getData(pathnotfoc)

    plotData(pathfoc,pathnotfoc,60)

    focused_avg_atte = np.mean(foc)
    focused_avg_med = np.mean(med)

    unfocused_avg_atte = np.mean(notfoc)
    unfocused_avg_med = np.mean(notmed)

    print("focused avg: focus %f, med %f"%(focused_avg_atte, focused_avg_med))
    print("unfocused avg: focus %f, med %f"%(unfocused_avg_atte, unfocused_avg_med))


def getData(path):
    dataset = pd.read_csv(path)
    dataset=dataset.values
    
    poor = dataset[:,0]
    raw = dataset[:, 1]
    focused_attention = dataset[:, 2]
    focused_meditation = dataset[:, 3] 
    return poor,raw,focused_attention,focused_meditation

def plotData(focused,notfocused,duration):#duration-->record time (sec)
    poor,raw,att1,med1=getData(focused)
    timeVector = np.linspace(0,duration,len(att1))# 1 minute
    poor,raw,att2,med2=getData(notfocused)
   
    plt.subplot(211)
    plt.title("Focused")
    plt.plot(timeVector, att1, "b", label="attention")
    plt.legend()

    timeVector = np.linspace(0,duration,len(att2))# 1 minute
    plt.subplot(212)
    plt.title("NotFocused")
    plt.plot(timeVector, att2, "b", label="attention")
    plt.legend()
    plt.show()





if __name__ == "__main__":
    main()